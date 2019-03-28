int h = hour();
int min = minute();
int seg = second();
float angleSec = (seg *TWO_PI)/60 -PI/2;
float angleMin = (min*60 *TWO_PI)/60 -PI/2;
float angleHour = (h*60*60 *TWO_PI)/60 -PI/2;
float div = TWO_PI/60;

int i=1;
void setup() {
  size(500,500);
}

void draw() {
  drawRelogio(250,250,250);
  attVariaveis();
  //println(seg);
  println(min);
  //println(h);
  drawSegundos(250,250,100,angleSec);
  drawMinutos(250,250,90,angleMin);
  drawHoras(250,250,70,angleHour);


    
}

void drawRelogio(float x, float y, float raio) {
 noStroke();
  fill(0);
  ellipse(x, y, raio, raio);
   fill(255);
  ellipse(x, y, raio-40, raio-40);
  for (float f = 0; f < 2*PI; f += div) {
    float Vx = x + cos(f) * (raio-150);
    float Vy = y + sin(f) * (raio-150);
    fill(0);
    ellipse(Vx, Vy, 3, 3);
 }
 
 for (float i = 0; i < 2*PI; i+= PI/2){
   float Px = x + cos(i) * (raio-150);
   float Py = y + sin(i) * (raio-150);
   fill(0,0,255);
   ellipse (Px, Py, 8,8);
 }
 
 for (float i = 0; i < 2*PI; i+= PI/6){
   float Px = x + cos(i) * (raio-150);
   float Py = y + sin(i) * (raio-150);
   fill(0,105,255);
   ellipse (Px, Py, 5,5);
 }
}

void drawHoras(float x, float y, float raio, float f) {
  noFill(); 
    float Vx = x + cos(f) * raio;
    float Vy = y + sin(f) * raio;
    stroke(0,255,0);
    strokeWeight(5);
    line(x,y,Vx,Vy);
   
}
void drawMinutos(float x, float y, float raio, float f) {
  noFill(); 
    float Vx = x + cos(f) * raio;
    float Vy = y + sin(f) * raio;
    stroke(255,0,0);
    strokeWeight(5);
    line(x,y,Vx,Vy);
   
}
void drawSegundos(float x, float y, float raio, float f) {
  noFill(); 
    float Vx = x + cos(f) * raio;
    float Vy = y + sin(f) * raio;
    stroke(0,0,255);
    strokeWeight(5);
    line(x,y,Vx,Vy);
   
}
void attVariaveis(){
  h =hour();
  min = minute();
  seg = second();
  angleSec = (seg *TWO_PI)/60 -PI/2;
  angleMin = (min*60 *TWO_PI)/3600 -PI/2;
  print(angleMin);
  angleHour = (h*60*60 *TWO_PI)/43200 -PI/2;
}
