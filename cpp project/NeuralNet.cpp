#include <vector>
#include <iostream>
#include <cstdlib>

using namespace std;

struct Connection
{
    double weight;
    double deltaWeight;
};

class Neuron;

typedef vector<Neuron> Layer;

/**************************** class Neuron ***************************/
class Neuron
{
    public:
        Neuron(unsigned numOutputs);

    private:
        static double randomWeight(void) { return rand() / double(RAND_MAX);}
        double m_outputVal;
        vector<Connection> m_outputWeights;
};

Neuron::Neuron(unsigned numOutputs)
{
    for (unsigned c = 0; c < numOutputs; ++c){
        m_outputWeights.push_back(Connection());
        m_outputWeights.back().weight = randomWeight();
    }
}

/***************************** class Net *****************************/
class Net {
    public:
        Net(const vector<unsigned> &topology);
        void feedForward(const vector<double> &inputVals) {};
        void backProp(const vector<double> &targetVals) {};
        void getResults(vector<double> &resultVals) const {};

    private:
        vector<Layer> m_layer; // m_layers[layerNum][neuronNum]
};

void feedForward(const vector<double> &inputVals)
{

};

Net::Net(const vector<unsigned> &topology)
{
    unsigned numLayers = topology.size();
    
    // create a new layer
    for (unsigned layerNum = 0; layerNum < numLayers; ++layerNum) {
        m_layer.push_back(Layer());
        unsigned numOutputs = layerNum == topology.size() - 1 ? 0 : topology[layerNum + 1];

        // fill the layer with neurons + bias
        for (unsigned neuronNum = 0; neuronNum <= topology[layerNum]; neuronNum++) {
            m_layer.back().push_back(Neuron(numOutputs));
            cout << "Made a Neuron!" << endl;
        }

    }
}

int main()
{
    vector<unsigned> topology;

    // e.g. {3,2,1}
    topology.push_back(3);
    topology.push_back(2);
    topology.push_back(1);

    Net myNet(topology);

    vector<double> inputVals;
    vector<double> targetVals;
    vector<double> resultVals;
    
    myNet.feedForward(inputVals);
    myNet.backProp(targetVals);
    myNet.getResults(resultVals);
}