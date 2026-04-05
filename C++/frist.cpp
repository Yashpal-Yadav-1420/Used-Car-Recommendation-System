/*#include<iostream>
using namespace std;
int main(){
 cout<<"Hello World";
 return 0;   
}*/
#include <dlib/svm.h>
#include <dlib/data_io.h>
#include <dlib/matrix.h>

using namespace dlib;

int main() {
    typedef matrix<double, 2, 1> sample_type;
    typedef radial_basis_kernel<sample_type> kernel_type;

    // Create a training dataset
    std::vector<sample_type> samples;
    std::vector<double> labels;
    
    // Fill dataset
    // ...

    // Train the SVM
    svm_c_trainer<kernel_type> trainer;
    trainer.set_kernel(kernel_type(0.1));
    decision_function<kernel_type> dec_func = trainer.train(samples, labels);

    // Use the model
    sample_type sample;
    sample(0) = 1.0;
    sample(1) = 2.0;
    double result = dec_func(sample);
    
    std::cout << "Prediction: " << result << std::endl;
    return 0;
}
