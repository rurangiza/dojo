
#include <iostream>
#include <cmath>
#include <fstream>
using namespace std;

const int sampleRate = 44100;
int

class SineOscillator {
    float frequency, amplitude, angle = 0.0f, offset = 0.0;

    public:
        SineOscillator(float freq, float amp) : frequency(freq), amplitude(amp) {
            offset = 2 * M_PI * frequency / sampleRate;
        }
        float process() {
            auto sample = amplitude * sin(angle);
            angle += offset;
            return sample;
            // A * sin(2*PI*Freq/sample_rate)
        }
};

int main() {
    SineOscillator sineOscillator(440, 0.5);
    ofstream audioFile;
    audioFile.open("waveform", ios::binary);

    int duration = 2;
    for (int i = 0; i < sampleRate * duration; i++) {
        audioFile << sineOscillator.process() << endl;
    }

    cout << "Float size: " << sizeof(float) << endl;
    cout << "Int size: " << sizeof(int) << endl;

    audioFile.close();
    return 0;
}