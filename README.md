
<img src='figs/readme/rookie_2.png'>
### CNNs in the Frequency Domain

<p>&nbsp;

### Motivation and Background...
Certain biological systems measure and calculate responses after transforming the environmental signals from time-dependent to frequency-dependent representations.  The auditory system in mammals, for example, includes a structure in which changes in air pressure cause a resonant response at different physical locations.  As such, the tiny hairs located at a given location will move in response to a specific sound frequency.  As the hair movements trigger a response to different nerves, the brain essentially receives auditory information in the frequency domain.  

Similarly, sensory neurons in the skin which detect relative temperature fire at a rate proportional to the temperature difference; high difference (hot or cold) from their previous state results in faster firings.

**For some reason, Nature has chosen to process certain inputs in frequency space.  And perhaps there is a built-in efficiency that we can exploit for more general signal processing.**



<table><tr>
<td><img src='figs/readme/sawtooth/256/sawtooth_11025_5706_256.png'></td>
<td><img src='figs/readme/sawtooth/256/sawtooth_12385_5540_256.png'>
<td><img src='figs/readme/sawtooth/256/sawtooth_12716_9973_256.png'>
<td><img src='figs/readme/sawtooth/256/sawtooth_15391_4238_256.png'>
<td><img src='figs/readme/sawtooth/256/sawtooth_18736_8911_256.png'></tr>
<tr>
<td><center>11025 Hz</center></td>
<td><center>12385 Hz</center></td>
<td><center>12716 Hz</center></td>
<td><center>15391 Hz</center></td>
<td><center>18736 Hz</center></td></tr>
<tr>
<td><img src='figs/readme/square/256/square_11025_5706_256.png'> </td>
<td><img src='figs/readme/square/256/square_12385_5540_256.png'> </td>
<td><img src='figs/readme/square/256/square_12716_9973_256.png'> </td>
<td><img src='figs/readme/square/256/square_15391_4238_256.png'> </td>
<td><img src='figs/readme/square/256/square_18736_8911_256.png'> </td>
</tr></table>
<p>&nbsp;
<table><tr>
<td><img src='figs/readme/dirty_5k/sawtooth/sawtooth_2195_9879_256.png'></td>
<td><img src='figs/readme/dirty_5k/sawtooth/sawtooth_2319_2718_256.png'>
<td><img src='figs/readme/dirty_5k/sawtooth/sawtooth_3445_6854_256.png'>
<td><img src='figs/readme/dirty_5k/sawtooth/sawtooth_3445_6854_256.png'>
<td><img src='figs/readme/dirty_5k/sawtooth/sawtooth_4874_8253_256.png'></tr>
<tr>
<td><center>2195 Hz</center></td>
<td><center>2319 Hz</center></td>
<td><center>3445 Hz</center></td>
<td><center>3691 Hz</center></td>
<td><center>4874 Hz</center></td></tr>
<tr>
<td><img src='figs/readme/dirty_5k/square/square_2195_9879_256.png'> </td>
<td><img src='figs/readme/dirty_5k/square/square_2319_2718_256.png'> </td>
<td><img src='figs/readme/dirty_5k/square/square_3445_6854_256.png'> </td>
<td><img src='figs/readme/dirty_5k/square/square_3691_1252_256.png'> </td>
<td><img src='figs/readme/dirty_5k/square/square_4874_8253_256.png'> </td>
</tr></table>
<p>&nbsp;

<table>
<tr colspan = 10>
<td><img src='figs/readme/dirty_5k/sawtooth/sawtooth_2037_4414_64.png'></td>
<td><img src='figs/readme/dirty_5k/sawtooth/sawtooth_2167_6525_64.png'></td>
<td><img src='figs/readme/dirty_5k/sawtooth/sawtooth_2248_5151_64.png'></td>
<td><img src='figs/readme/dirty_5k/sawtooth/sawtooth_2902_3732_64.png'></td>
<td><img src='figs/readme/dirty_5k/sawtooth/sawtooth_3019_9176_64.png'></td>

<td><img src='figs/readme/dirty_5k/sawtooth/sawtooth_3117_3631_64.png'></td>
<td><img src='figs/readme/dirty_5k/sawtooth/sawtooth_4067_6719_64.png'></td>
<td><img src='figs/readme/dirty_5k/sawtooth/sawtooth_4097_2118_64.png'></td>
<td><img src='figs/readme/dirty_5k/sawtooth/sawtooth_4102_9135_64.png'></td>
<td><img src='figs/readme/dirty_5k/sawtooth/sawtooth_4234_1087_64.png'></td></tr>
<tr colspan = 10>
<td><img src='figs/readme/dirty_5k/square/square_2037_4414_64.png'></td>
<td><img src='figs/readme/dirty_5k/square/square_2167_6525_64.png'></td>
<td><img src='figs/readme/dirty_5k/square/square_2248_5151_64.png'></td>
<td><img src='figs/readme/dirty_5k/square/square_2902_3732_64.png'></td>
<td><img src='figs/readme/dirty_5k/square/square_3019_9176_64.png'></td>

<td><img src='figs/readme/dirty_5k/square/square_3117_3631_64.png'></td>
<td><img src='figs/readme/dirty_5k/square/square_4067_6719_64.png'></td>
<td><img src='figs/readme/dirty_5k/square/square_4097_2118_64.png'></td>
<td><img src='figs/readme/dirty_5k/square/square_4102_9135_64.png'></td>
<td><img src='figs/readme/dirty_5k/square/square_4234_1087_64.png'></td></tr>
</table>'
### Investigation...
Step 1 is EDA.
No datasets, so generate sine waves and make them dirty.
<src = 'clean sine wave'>   ==>  <src='dirty sine wave'>
<src = 'clean sine waves'>  ==>  <src='dirty sine waves'>

Sent these into Fast Fourier Transform function.
fourier = np.fft.fft(wave)
<src = 'ft of 1 sine'>  ==> <src = 'ft of higher f'>
<src = 'ft of 1 dirty'> ==> <src = 'ft of many dirty fs'>

Looked hopeful that we can extract information if we analyze data in the frequency space and then perform some type of identification/categorization using a convolutional neural network.

Bossman kept asking for a target... what is the plan here?

Scipy.signal can generate two other periodic waveforms out of the box:
sawtooth <img src = 'sawtooth'>
square <img src = 'square'>

Just to be a little fair:  make them dirty
<img src='dirty sawtooth'>
<img src='dirty square'>

Goal: Train a CNN to recognize and perform binary categorization of sawtooth and square waves that have been transformed to the frequency domain.  

More explicitly, use a 2-D image representation of the waveform {what you see above}.  

Task: create the square and sawtooth FFT data.  
Pick a square image size (ie 64 x 64).
Shrink down the FFT values array to *image size* entries by summing adjacent values.
Standardize by normalizing and multiplying by *image size*.
Turn this smaller array into horizontally stacked columns filled from the bottom with ones to height proportional to the value; pad remainder of array with zeros.
Save each image.  
Ultimately create 5000 samples of each type for training, and 1000 of each type for testing.

The CNN:
Started with a CNN modeled from the cat-dog classifier from class.  Used "flow_from_directory" to keep process standardized during the process of choosing image and sample sizes.

Added ImageDataGenerator to augment the dataset.  
Conv2D with 32 layers, RELU activation
(3x3) & (4x4) filters, depending on dataset under test;
MaxPooling2D pool_size = 2x2
Dropout .1 - .25 for best performance (loss downward)
Flatten
Dense = 128 with RELU
Dense final with SIGMOID
Optimizer = adam; loss = binary_crossentropy

Performance:
Ran 30 epochs on 10k image train, 2k test.  Reached 99% accuracy, ~20 epochs; loss continued to slowly drop.
Saw damped oscillatory pattern as accuracy continued to climb.

def sine(f, t):
    return np.sin(2*np.pi*f*t)

def sawtooth(f, t):
    return sg.sawtooth(2*np.pi*f*t)

def square(f, t):
    return sg.square(2*np.pi*f*t)

==>
*
<p>&nbsp;

### Start the EDA...

<p>&nbsp;

### Graphing by the 1000's...
<table>
</table>

<p>&nbsp;

### Gathering Data...
<p>&nbsp;


### Results...
<p>&nbsp;

### Looking Ahead...

<p>&nbsp;

### Data Sources...
Many Thanks to:
