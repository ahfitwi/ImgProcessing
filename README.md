# ImgProcessing
Micellaneous Image Processing Methods and Techniques.
- **Errode**: An erosion eats away at the foreground pixels thereby decreasing the size of the foreground object.
  - img = cv2.erode(img, np.ones([3,3], np.uint8), iterations = 3)
- **Dilate**: The opposite of an erosion is a dilation. A dilation grows the foreground pixels thereby increasing the size of foreground objects
    - Especially useful for joining broken parts of an image together
    - img = cv2.dilate(img, np.ones([3, 3], np.uint8), iterations= 3)
- **Distortion**: https://www.edmundoptics.com/knowledge-center/application-notes/imaging/distortion/
- **Angular Resolution**: How do you calculate angular resolution? To calculate angular resolution, use the formula: $\theta = \frac{1.22\lambda} { d}$. where λ is
- the wavelength of light and d is the diameter of the lens aperture.
- What does angular resolution measure? Angular resolution is a major determinant of image resolution. It is the capacity of an image-forming device
  such as an optical or radio telescope, a microscope, a camera, or an eye, to separate two objects located at a small angular distance.
- Where does the 1.22 come from in the formula for angular resolution? The factor 1.22 in the angular resolution formula is derived from a
  calculation of the position of the first dark ring surrounding the central Airy disc of the diffraction pattern.
  What is the resolution formula? To calculate angular resolution, use the formula: $\theta = \frac{1.22\lambda} { d}$. where λ is the wavelength of light and d is the diameter of the lens aperture.
- **Lens Maker Equation**: Describes the relationship between focal length, radii of curvatures, and the material the lens operates.
$$\frac{1}{f}\ =\ (n - 1)(\frac{1}{R1} - \frac{1}{r2})$$ 
- where R1 and R2 are the radii of curvature, f is the focal length, and n is the index of refraction.
- If the lens is operating in air, then with $n_0 = 1$,  this formula will simplify.
  $$\frac{1}{f}\ =\ (n - 1)(\frac{1}{R1} - \frac{1}{r2})$$
-  From (http://www.physicsbootcamp.org/lens-maker-equation.html#:~:text=1)%201%20f%20%3D%20(%20n,on%20left%20then%20R%3C0.)
- $$\frac{1}{f}\ =\ \frac{(n_1 - n_0)}{n_0}(\frac{1}{R1} - \frac{1}{R2})$$
- If d is not negligible:
  $$\frac{1}{f}\ =[n_1 - 1][\frac{1}{R1} - \frac{1}{R2} + \frac{(n-1)d}{nR_1 R_2}]$$
- If d is not negligible and lens is in a medium (for instance water):
  $$\frac{1}{f}\ =[\frac{n_l - n_m}{n_m}][\frac{1}{R1} - \frac{1}{R2} + \frac{(\frac{n_l - n_m}{n_m})d}{n_lR_1 R_2}]$$
  $$\frac{1}{f}\ =[\frac{n_l }{n_m}-1][\frac{1}{R_1} - \frac{1}{R_2} + \frac{(\frac{n_l }{n_m}-1)d}{n_lR_1 R_2}]$$
 https://www.youtube.com/watch?v=uPMztgFwsGU

  
