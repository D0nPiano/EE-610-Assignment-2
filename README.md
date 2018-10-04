EE610 Image Processing

Assignment 2, September 2018, IMAGE RESTORATION

Notes:  Team size 1 => Do tasks (1 or 2 or 3) and 4.

Team size 2 => Do tasks 1 and 2 and 4.

Team size 3 or more => Do all tasks.

 

1.       Deblurring when you know the blur kernel:

a.       Refer to: http://webdav.is.mpg.de/pixel/benchmark4camerashake/

b.      Take images blurred by kernel 1 – 4. Assume spatially invariant kernel

c.       Implement a full inverse filter to deblur the image; apply separately to RGB

d.      Implement a truncated inverse filter to deblur the image. What is a good radius for truncation in the Fourier domain? What is the PSNR? What is the SSIM? Make truncation interactive.

e.      Implement an approximate Weiner filter to deblur the image. What is a good value of K? What is the PSNR? What is the SSIM? Make K interactive.

f.        Implement a constrained least square filter to deblur the image. What is a good value of γ? What is the PSNR? What is the SSIM? Make γ interactive.

g.       Take one of your own photographs, estimate the kernel, and apply the best technique. You cannot compute the PSNR or SSIM as you don’t know the ground truth.


2.       Blind deblurring using ML when you don’t know the blur kernel:

a.       Take several images

b.      Blur them by several blur kernels involving both defocusing and shakes

c.       Sample paired patches of sharp and blurred images

d.      Learn a function to predict the central pixel of the clean image using a patch surrounding the corresponding pixel in the blurred image. See for example: https://papers.nips.cc/paper/5485-deep-convolutional-neural-network-for-image-deconvolution.pdf

e.      If the results are not satisfactory, try restricting to a small set of shakes and blurs (e.g. PSF that can be captured within a 9x9 window)

f.        Remember to add some noise so that ML learns that too.

g.       Apply the function to the images given in the paper using the first four blur kernels. What is the PSNR? What is the SSIM?

h.      Take some of your own photographs, estimate the kernel, and apply your technique. You cannot compute the PSNR or SSIM as you don’t know the ground truth.


3.       Implement an advanced image restoration technique of your choice from a research paper.


4.       Write a report in IEEE paper format with the following sections (submit pdf document):

a.       Introduction: Describe the problem of deblurring with the degradation model, why it is an important problem, why it is a difficult problem, and what kind of things you tried

b.      Background and related work:

                                                               i.      Describe various approaches briefly (one para/subsection each) when the kernel is known

                                                             ii.      Briefly describe the ML approaches, and the specific approach that you tried

                                                            iii.      Describe any other approach that you tried

c.       Experiments and Results: Describe experiments results, including when each technique performs well, and when it breaks down, and show with sample resultant images and tables to compare techniques (e.g. using PSNR and SSIM)

d.      Discussion and conclusions: Write a discussion of what you learnt and what are the current directions in image restoration (assuming blurring and noise)

e.      Links: Add a link to your code on GitHub (clearly indicate which line you wrote yourself. We will assume other lines were copied from the indicated source), and to a video of your demo.

f.        References: List of material read and codes referred. Note that the report has to be written in your own words. Nowhere should more than a few words appear to be copied from somewhere else.
