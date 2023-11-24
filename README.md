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
  calculation of the position of the first dark ring surrounding the central Airy disc of the diffraction pattern. What is the resolution formula?
- To calculate angular resolution, use the formula: θ = 1.22 * λ / d. where λ is the wavelength of light and d is the diameter of the lens aperture.
