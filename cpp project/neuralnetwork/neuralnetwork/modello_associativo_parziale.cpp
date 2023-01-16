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

#define n_neuron 3

using namespace std;

//Protorypes
void vector_dot_Tvector(double res[][n_neuron], double a[n_neuron], double Tb[n_neuron]);
vector<double> Tensor(vector<double>tensor);
void matrix_to_vector(double w[][n_neuron], double v[]);
void print_matrix(double x[], int r, int c, int R, int C);

int main()
{
//Define input tensor
    double f1[n_neuron] = {1,2,3};
    double f2[n_neuron] = {1,2,3};
    double f3[n_neuron] = {1,2,3};
    
//Define output tensor
    double g1[n_neuron] = {1,2,3};
    double g2[n_neuron] = {1,2,3};
    double g3[n_neuron] = {1,2,3};
    
//Predefine weights matrix
    double DA1[n_neuron][n_neuron];
    double DA2[n_neuron][n_neuron];
    double DA3[n_neuron][n_neuron];
    
//Other predefinition
    double v[n_neuron*n_neuron];
    
    vector_dot_Tvector(DA1, g1, f1);
    matrix_to_vector(DA1, v);
    
    return 0;
};

void vector_dot_Tvector(double res[][n_neuron], double a[n_neuron], double Tb[n_neuron])
{
    for(int i=0; i<n_neuron; i++) {
        for(int j=0; j<n_neuron; j++) {
            res[i][j] = a[i]*Tb[j];
        }
    }
};

void matrix_to_vector(double w[][n_neuron], double v[])
{
    int r, c, k;
    r=c=n_neuron;
    for(int i=0; i<r; i++){
        for(int j=0; j<c; j++){
            k = i*3 + j;
            v[k] = w[i][j];
        }
    }
};

void print_matrix(double x[], int r, int c, int R, int C)
{
    for(int i=0; i<r; i++) {
        for(int j=0; j<0; j++) {
            double gl;
            gl = x[i*c+j];
            if(gl>=0) {
                printf("\x1b[%d;%dH%0.1lf \x1b[0m ", i*2+R, 6*j+C, gl);
            } else {
                printf("\x1b[%d;%dH%0.1lf \x1b[0m ", i*2+R, 6*j+C-1, gl);
            }
            
        }
        fflush(stdout);
    }
};

vector<double> Tensor(vector<double>tensor)
{
    vector<double> Vector;
    vector<double>::size_type size = tensor.size();
    
    for(int i=0; i<size; i++){
        Vector.push_back(tensor[i]);
    }
    return Vector;
}
