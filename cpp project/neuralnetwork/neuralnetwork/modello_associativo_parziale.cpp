//
//  main.cpp
//  neuralnetwork
//
//  Created by Federico Moretta on 14/01/23.
//  Neural Network for machine learning

#include <iostream>
#include <vector>
#include <stdio.h>
#include <math.h>
#include <fstream>
#include <stdlib.h>

#define n_input 3
#define n_output 3

using namespace std;

//typedef the tensors 1D and 2D
typedef vector<double> tensor;
typedef vector< vector<double> > tensor2d;

//Protorypes
tensor2d tensor_dot_Ttensor(tensor a, tensor Tb);
tensor tensor2d_dot_tensor(tensor2d A, tensor b);
tensor Tensor(double fill_in[], int size);
tensor2d tensor2d_sum(tensor2d A, tensor2d B);
tensor2d Tensor2d(double col_val[], int rows, int cols);
void print_tensor2d(tensor2d x);
void print_tensor(tensor x);
double getX(tensor a, tensor b);

int main()
{
//Define input tensor
    double f1[n_input] = {1,0,1};
    double f2[n_input] = {1,0,-1};
    double f3[n_input] = {0,1,0};
    
//Define output tensor
    double g1[n_output] = {1,1,0};
    double g2[n_output] = {1,0,1};
    double g3[n_output] = {0,0,1};

    tensor F1 = Tensor(f1, 3);
    tensor G1 = Tensor(g1, 3);

    tensor F2 = Tensor(f2, 3);
    tensor G2 = Tensor(g2, 3);

    tensor F3 = Tensor(f3, 3);
    tensor G3 = Tensor(g3, 3);

// first step: create weights matrix
    tensor2d A1 = tensor_dot_Ttensor(G1, F1);
    tensor2d A2 = tensor_dot_Ttensor(G2, F2);
    tensor2d A3 = tensor_dot_Ttensor(G3, F3);

// second step: create global weights matrix
    tensor2d A1A2 = tensor2d_sum(A1, A2);
    tensor2d Atot = tensor2d_sum(A1A2, A3);

// third step: find the linear proportional coefficient
    tensor b1 = tensor2d_dot_tensor(Atot, F1);
    tensor b2 = tensor2d_dot_tensor(Atot, F2);
    tensor b3 = tensor2d_dot_tensor(Atot, F3);

    double etha_1 = getX(G1, b1);
    double etha_2 = getX(G2, b2);
    double etha_3 = getX(G3, b3);

    cout << etha_1 << endl;
    cout << etha_2 << endl;
    cout << etha_3 << endl;
    
    return 0;
};

tensor2d tensor_dot_Ttensor(tensor a, tensor Tb)
{
    tensor2d res;
    for(int i=0; i<a.size(); i++) { 
        tensor row;
        for(int j=0; j<Tb.size(); j++) {
            row.push_back(a[i]*Tb[j]);
        }
        res.push_back(row);
    }
    return res;
};

// sum of matrices
tensor2d tensor2d_sum(tensor2d A, tensor2d B) {

    tensor2d C;
    for(int i=0; i<A.size(); i++) {
        tensor row;
        for(int j=0; j<A[i].size(); j++) {
            row.push_back(A[i][j] + B[i][j]);
        }
        C.push_back(row); // incassa la riga
    }
    return C;
}

tensor tensor2d_dot_tensor(tensor2d A, tensor b) {

    tensor c;
    for(int i=0; i<A.size(); i++) {
        double val = 0;
        for(int j=0; j<b.size(); j++) {
            val += A[i][j]*b[j];
        }
        c.push_back(val);
    }
    return c;
}

// create vector based tensors containers
tensor Tensor(double fill_in[], int size) {

    tensor tensor;
    for(int i=0; i<size; i++) {
        tensor.push_back(fill_in[i]);
    }
    return tensor;
}

// create vector based tensors containers in 2D dimension
tensor2d Tensor2d(double col_val[], int rows, int cols) {

    tensor2d tensor2d;
    for (int i = 0; i < rows; i++) {
        // Vector to store column elements
        tensor row;

        for (int j = 0; j < cols; j++) {
            row.push_back(col_val[j]);
        }

        // Pushing back above 1D vector
        // to create the 2D vector
        tensor2d.push_back(row);
    }
    return tensor2d;
}

// print on command window
void print_tensor2d(tensor2d x) {
    for (int i = 0; i < x.size(); i++) {
        for (int j = 0; j < x[i].size(); j++)
            cout << x[i][j] << " ";
        cout << endl;
    }
    cout << endl;
}

void print_tensor(tensor x) {
    for(int i = 0; i < x.size(); i++) {
        cout << x[i] << endl;
    }
    cout << endl;
}

double getX(tensor a, tensor b) {
    if (a.size() != b.size()) return 0; 
    for( int i=0; i<a.size(); i++ ){
       if(a[i] != 0) {
            return b[i] / a[i];
       } 
    }
    return 0;
}