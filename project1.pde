// MANUAL CONTROLS
// WS to ++/-- speed
// AD to ++/-- tilt
// Space to shoot projectile
// E to exit()

// Genome size and number of cannons
final int cannon_genome = 10;
final int cannon_sample = 50;

// Target size and
final int target_size = 200;

// Used to randomly evolve based on fitness
final float change_speed = 0.05;
final float change_tilt = 0.05;

// Shoots every 500ms
final int shot_interval = 500;
int prev_time = 0;

//final int target_sample = 10;
String[] bases = {"A", "C"};

ArrayList<Cannonball> projectiles;
Cannon[] cannons;

Target target;

void setup() {
  size(1440, 800);
  smooth();
  rectMode(CENTER);
  
  cannons = new Cannon[cannon_sample];
  for (int i = 0; i < cannon_sample; i++)
  {
    cannons[i] = new Cannon(width / 4, height - 50);
  }
  
  //test = new Cannon( width / 4, height - 50);
  target = new Target(width - 200, height - 500);
  projectiles = new ArrayList<Cannonball>();
  for (int i = 0; i < cannons.length; i++) {
    cannons[i].calcFitness();
    cannons[i].print();
  }

}

void draw()
{
  background(200);
  
  for (int i = 0; i < cannons.length; i++) {
    cannons[i].display();
  }
  
  target.display();
  
  // Check and update projectiles & collisions 
  for (int i = 0; i < projectiles.size(); i++) 
  {
   Cannonball p = projectiles.get(i);
   p.update();
   p.display();
  
   if (target.collision(p)) {
     target.target_hit();
     projectiles.remove(i);
     //target.display();
     //delay(3000);
     //exit();
    }
    if (p.offScreen()) {
      projectiles.remove(i);
    }
  }
  
  if (millis() - prev_time >= shot_interval) {
    prev_time = millis();  // Update the last shot time
    shoot_cannons();  // Trigger shooting
  }
  evolve_cannons();
}


void shoot_cannons() {
  for (int i = 0; i < cannons.length; i++) {
    projectiles.add(cannons[i].fire());  // Fire each cannon
  }
}

// Fake evolution
void evolve_cannons()
{
  for (int i = 0; i < cannons.length; i++) {
      int randNum = int(random(0, 4));  // Generate a random number between 0 and 3
  
      switch(randNum) {
        case 0:
          cannons[i].evolve(0, -cannons[i].fitness*change_tilt);
          break;
        case 1:
          cannons[i].evolve(0, cannons[i].fitness*change_tilt);
          break;
        case 2:
          cannons[i].evolve(cannons[i].fitness*change_speed, 0);
          break;
        case 3:
          cannons[i].evolve(-cannons[i].fitness*change_speed, 0);
          break;
        default:
          println("Error, default case");
          break;
      }
  }
}

// Key presses
void keyPressed() {
  if (key == 'e') exit();
  if (key == ' ') { // Fire when spacebar is pressed
    for (int i = 0; i < cannons.length; i++) {
      projectiles.add(cannons[i].fire());
    }
  }
  // TILT
  if (key == 'a') {
    for (int i = 0; i < cannons.length; i++) {
      cannons[i].evolve(0, cannons[i].fitness*change_tilt);
    }
  }
  if (key == 'd') {
    for (int i = 0; i < cannons.length; i++) {
      cannons[i].evolve(0, -cannons[i].fitness*change_tilt);
    }
  }
  // SPEED
  if (key == 'w') {
    for (int i = 0; i < cannons.length; i++) {
      cannons[i].evolve(cannons[i].fitness*change_speed, 0);
    }
  }
  if (key == 's') {
    for (int i = 0; i < cannons.length; i++) {
      cannons[i].evolve(-cannons[i].fitness*change_speed, 0);
    }
  }
}

// PROJECTILES
class Cannonball
{
  float x, y;
  float vx, vy;
  float gravity = 0.2;
  color ball_color = color(0, 255, 0);
  
  Cannonball(float x, float y, float vx, float vy) {
    this.x = x;
    this.y = y;
    this.vx = vx;
    this.vy = vy;
  }
  
  void update() {
    x += vx;
    y += vy;
    vy += gravity;
  }
  
  void display() {
   fill(ball_color);
   ellipse( x, y, 10, 10);
  }
  
  // Check if the projectile is off-screen
  boolean offScreen() {
    return x < 0 || x > width || y > height;
  }
}
// TARGET CLASS
class Target
{
  float x, y;
  float size;
  color target_color;
  
  Target(float x, float y) {
    this.x = x;
    this.y = y;
    this.size = target_size;
    target_color = color(255, 0, 0);  // Red color
  }
  
  void display() {
     fill(target_color);
     ellipse(x, y, size, size);
  }
  
  boolean collision(Cannonball c)
  {
     float distance = dist(c.x, c.y, x, y);
     return distance < size / 2;
  }
  void target_hit() {
    target_color = color(0, 0, 255); // Change color
  }
}
// CANNON CLASS
class Cannon {
  float x, y;
  float size;
  color cannon_color = color(128);
  float tilt;
  float speed;
  
  ArrayList<String> genome;
  int fitness;

  Cannon(float x, float y) {
    this.x = x;
    this.y = y;
    this.tilt = -PI / 4; // 90 degrees. Change by genome
    this.speed = 10;
    genome = new ArrayList<String>();
    fitness = 0;
    for (int i = 0; i < cannon_genome; i++) {
      genome.add(bases[(int)random(2)]);
    }
  }

  void display() {
    pushMatrix();
    fill(cannon_color);
    translate(x, y);
    rotate(tilt);
    rect(-15, -10, 30, 20); // Cannon body
    line(0, 0, 50, 0); // Cannon barrel
    popMatrix(); 
  }

  // Fire projectiles 
  Cannonball fire()
  {
    float vx = cos(tilt) * speed;
    float vy = sin(tilt) * speed;
    return new Cannonball(x + 50, y, vx, vy);
  }
  // Function to print the genome and fitness
  void print() {
    println(genome);
    println("fitness = " + fitness);
  }

  // Override toString method to return the genome and fitness as a string
  String toString() {
    String returnStr = "" + genome;
    returnStr += "\nfitness = " + fitness;
    return returnStr;
  }

  // Function to calculate fitness
  void calcFitness() {
    for (int i = 0; i < (genome.size() - 1); i++) {
      //String str = genome.get(i) + genome.get(i + 1);
      if (genome.get(i) == ("A")) {
        fitness++;
        continue;
      }
      if (genome.get(i) == ("C")) {
        fitness--;
      }
    }
  }
  
  void evolve(float s, float t) {
     this.tilt += t;
     this.speed += s;
  }
}
