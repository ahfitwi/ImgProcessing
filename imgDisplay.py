def plot_imgs(titles, images, cols):
        """Plots and Displays Multiple Images in RxC
           Created by Alem Fitwi, 29 July 2022
        """
        row = int(math.ceil(len(titles)/float(cols)))
        plt.figure(figsize=(4*cols, row*2), dpi=300)
        for i in range(len(titles)):
            plt.subplot(row,cols,i+1)
            plt.imshow(images[i],'gray')
            plt.title(titles[i])
            plt.xticks([])
            plt.yticks([])   
        #plt.savefig("img.jpg", dpi=300)
        plt.show()
