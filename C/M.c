//#include <stdio.h>
//#include <math.h>
//int main(){
    // printf("%d",'0' + 5);
   //int a = 5;
   //int b = (a >= 0) ? ((a % 2 == 0) ? 10 : 20) : ((a % 2 == 0) ? 30 : 40);
  // printf("%d",b);

    //int a = 5;  // 0101 in binary
    //int b = 3;  // 0011 in binary
    // int result = (a & b) + (a | b);
    //printf("%d", result);

    //int a, b, c, d;
    //a = b = c = d = 3; // Check here
    //a += b += c += d += 2;
    //printf("%d",a + b + c + d);

    //int a = 4, b = 1, c;
    //c = (--a == 3) || (b++ == 2);
    //printf("%d", a + b + c);

    //int a = 2, b = 3, c = 4;
    //c = (a++ != b) && (--c == a);
    //printf("%d", a + b + c);
    //int y = 2;
    //int x = 2;

    //printf("%d", (y = 2 * x) && (++y > 4));

    //int a = 4, b = 6;
    //int result = ++a + b--;
     //int z = x % y + x / y * y;
     //int result = 18 - 6 / 3 * 4 + 2;
     //printf("%d", result);
    //double a,b,c,x1,x2;
    //printf("Enter a: ");
    //scanf("%lf", &a);
    //printf("Enter b: ");
    //scanf("%lf", &b);
    //printf("Enter c: ");
    //scanf("%lf", &c);

    //x1 = (-b+sqrt((b*b)-4*a*c)/2*a);
    //x2 = (-b-sqrt((b*b)-4*a*c)/2*a);

    //printf("Value of x1: %.2lf\n", x1);
    //printf("Value of x2: %.2lf", x2);

    //x1 = (-b + sqrt((b*b) - 4*a*c) / 2*a);
    //x2 = (-b - sqrt((b*b) - 4*a*c) / 2*a);

    //printf("Value of x1: %.2lf\n", x1);
    //printf("Value of x2: %.2lf\n", x2);
    //int sum = 0;
    //for (int i = 2; i <= 8; i++) {
        //if (i % 2 == 0) {
            //sum += i;
        //}
   // }
    //printf("%d", sum);
    //int x = 3, y = 8;

    //if (x++ < 3)
        //x++;
        //y++;

    //printf("%d %d\n", x, y);

    //int i = 2;
    //for (; i <= 10; i++) {
        //printf("%d ", i);
        //i++;
    //}

    //int y = 3;
    //do {
       // y--;
    //} while (y--);
    //printf("%d", y);

   //int num; 
   //int s = 0;
   //scanf("%d", &num);
   
   //while (num > 0) 
   //{
 	//int d = num % 10;
 	//if (d % 2 != 0) 
 	//{
   	    //s += d;
 	//}
 	//num /= 10;
   //}
  
   //printf("%d\n", s);

   //for (int i = 4; i >= 2; i--) {
        //for (int j = i; j <= 15; j += 3); 
        //{
            //printf("Hello C\n");
        //}
        //printf("Hello C\n");
    //}
    //int i = 0;

    //for ( ; i < 5; )
    //{
        //printf("%d ", i);
        //i++;
    //}

    //int p, q, r;
    //scanf("%d %d %d", &p, &q, &r);
 
    //if (p)
        //if (q)
            //printf("X");
        //else if (r)
            //printf("Y");
        //else
            //printf("Z");
    //else
        //printf("W");
    //int a = 5;
    //for (int i = 1; i <= 6; i++) {
        //if (i % 2 != 0) {
            //a += i;
        //} else {
           // a -= i;
        //}
    //}
    //printf("%d", a);

    //int x = 2, y = 3;

    //if (x > 2 && y++ < 4)
        //printf("A");
    //else if (x < 3 || y < 5)
       // printf("B");
    //else
        //printf("C");

    //printf(" %d", y);

    //int i, j, sum = 0;

    //for (i = 1, j = 10; i < j; i += 2, j -= 2) {
        //sum += i * j;
    //}

    //printf("%d", sum);

    //int i, j;
    //for (i = 1; i <= 3; i++) {
        //for (j = 1; j <= 2; j++) {
            //switch (i + j) {
                //case 2:
                    //printf("A");
                //case 3:
                    //printf("B");
                    //break;
                //case 4:
                    //printf("C");
                //default:
                    //printf("D");
            //}
        //}
    //}

    //int n;
    //scanf("%d", &n);

    // Handle the case where n is less than 2
    //if (n < 2) {
        //printf("%d is not a prime number\n", n);
       // return 0;
    //}

    //int i;
    //for (i = 2; i <= sqrt(n); i++) {
        //if (n % i == 0) {
           // printf("%d is not a prime number\n", n);
           // return 0;
       // }
   // }

    //printf("%d is a prime number\n", n);
//--------------------------------------------------------------------------------------------------------------------------
    // Triangle code
    //int a,b,c;
    //scanf("%d",&a);
    //scanf("%d",&b);
    //scanf("%d",&c);
    //if((c*c)==(a*a)+(b*b)){
        //printf("YES");
    //}else{
        //printf("NO");
    //}
//-------------------------------------------------------------------------------------------------------------------------
// Coordinate//
    //double a,b;
    //scanf("%lf",&a);
    //scanf("%lf",&b);
    //if(a>0){
        //if(b>0){
            //printf("First");
        //}else{
            //printf("Fourth");
        //}
    //}else if (a<0){
        //if(b>0){
            //printf("Second");
        //}else{
            //printf("Third");
        //}
    //}else if (a==0 || b==0){
        //if(b>0){
            //printf("y-axis");
        //}else if (b<0){
            //printf("-y-axis");
        //}else if (a>0){
            //printf("x-axis");
        //}else{
            //printf("-x-axis");
        //}    
    //}
    //else{
        //printf("Origin");
    //}
//--------------------------------------------------------------------------------------------------------------------------
   
   //double z,w;
   //scanf("%lf",&w);
   //scanf("%lf",&z);
   //if(z==1){
    //printf("%.2lf",w*5);
   //}else if (z==2){
    //printf("%.2lf",w*7);
   //}else if (z==3){
    //printf("%.2lf",w*10);
   //}else if (z==4){
    //printf("%.2lf",w*12);
   //}else if (z==5){
    //printf("%.2lf",w*16);
   //}else if (z==6){
    //printf("%.2lf",w*17);
   //}else if (z==7){
    //printf("%.2lf",w*19);
   //}
   //else if ((z<0 &&z>=8) && w<0){
    //printf("Invalid Input");
   //}
   
//-------------------------------------------------------------------------
// shopping
     //char s;
     //double a,n =0;
     //while (1){
        //scanf("%lf",&a);
        //scanf(" %c",&s);
        //n += a;
        //if(s=='y'){
        //}else{
            //break;
        //}
     //}
     //printf("%.2lf",n);

//-----------------------------------------------------------------------
     // Palindrome
     //int d,n=0,a=0,b;
     //scanf("%d",&d);
     //n=d;
     //while(d != 0)
     //{
         //b = d%10;
         //a = a*10 + b;
         //d = d/10;
     //}
     //if(a==n){
        //printf("%d is a palindrome number",n);
     //}else{
        //printf("%d is not a palindrome number",n);
     //}
// ----------------------------------------------------------------------
   // int a=1,b=1,x;
   // a+=b;
   // x= -a++ + b++;
   // printf("%d",x);


   // return 0;
//}