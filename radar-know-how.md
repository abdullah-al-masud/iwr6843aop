# Radar basics and in-depth theoretical discussion

## Radar basics

### Starting point

1. Range and velocity estimation basics: https://www.youtube.com/watch?v=-N7A5CIi0sg&t=784s
2. Angle estimation and beamforming basics: https://www.youtube.com/watch?v=GpXF4wVQ-L4
3. Overall basic breakdown of Range, Doppler, Angle calculation: https://www.youtube.com/watch?v=8cHACNNDWD8&t=150s
4. Control of beamforming: https://www.youtube.com/watch?v=VOGjHxlisyo&t=229s


## Summarized discussion

### Range-Doppler calculation
- FMCW (Frequency modulated Continuous Wave) radar: Radar which uses continuous wave to detect objects by using frequency modulation
- The carrier wave propagates through the space at a varying frequency (sawtooth modulation)
- A single increasing period of frequency increse is called a chirp
- FMCW radar uses Doppler shifts to understand a moving object
- Static objects can also be detected as the frequency is modulated which shows the response signal is shifted in time or in frequency or in both
    - If only shifted in time, the object is static
- To detect the object is moving towards or away, we need a complex IQ (In-phase-Quadrature) signal which has two components
    - Real signal
    - Imaginary signal (both are at 90 degree phase shift with each other)
- The distance of the object can be measured by d = c * t
- Range resolution is c / (2 * B), where c is speed of light and B is chirp bandwidth
- Velocity resolution depends on the frame time T
- The velocity of the object can be measured from the Doppler frequency (frequency shift) using Doppler equation
- When we want to measure range-velocity of multiple objects with a single transmitter-receiver antenna, we need to change the carrier signal from sawtooth to triangular modulation

### Angle estimation
- To detect the angle of the object, we can use a narrow-beam signal instead of omni-directional signal
- But it requires physical movement of the radar antenna
- We can use beam-forming technique by introducing multiple receiver antenna
- We place multiple receiver antenna at half wavelength distance from each other which causes a differential distance of d.sin(theta)
- If we form signal value (y) vs distance (x) map, and apply Fourier transofrmation on the derived signal along distance, we can get the angle estimation
- Angle resolution depends on the number of antenna
- Combining multiple transmitter and receiver creates a virtual antenna array which has same effect as a single transmitter with multiple receiver. For example, a transmitter with 8 receiver is equivalent to 2 transmitter with 4 receiver

### Beamforming
- Beamforming is a technique to control the direction of the signal to detect angle of detection
- Beamforming is done by allowing multiple receiver antenna
- If we change the gain (signal power) of the receiver antenna, the overall power of the beam can be controlled in different directions
- If we change the phase of the antenna, the beam can be rotated
- For a scan over 3D space to detect azimuth and elevation angles, we need a receiver antenna array positioned on a plane 


## More resources:
- Radar principles used in TI sensors
    1. https://www.ti.com/content/dam/videos/external-videos/ko-kr/2/3816841626001/5415203482001.mp4/subassets/mmwaveSensing-FMCW-offlineviewing_0.pdf
    2. https://dev.ti.com/tirex/explore/node?node=A__AXNV8Pc8F7j2TwsB7QnTDw__RADAR-ACADEMY__GwxShWe__2.10.00.2
    3. https://www.ti.com/lit/spyy005
- Radar signal power equation: https://www.mathworks.com/help/radar/ug/radar-equation.html?s_eid=PSM_15028
- 