# Hackerranklink: https://www.hackerrank.com/challenges/designer-pdf-viewer/problem?isFullScreen=true


def designerPdfViewer(h, word):
    temp = [h[ord(i)-ord("a")] for i in word]
    return max(temp)*len(word)

    
    
    
    
if __name__ == "__main__":
#     h = [i for i in range(0,26)]
    h = [1 ,3 ,1 ,3 ,1 ,4 ,1 ,3 ,2 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5, 5]
    word="abc"
    print(designerPdfViewer(h,word))