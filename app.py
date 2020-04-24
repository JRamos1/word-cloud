import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys

# # !jupyter nbextension install --py --user fileupload
# # !jupyter nbextension enable --py fileupload

# def _upload():

#     _upload_widget = fileupload.FileUploadWidget()

#     def _cb(change):
#         global file_contents
#         decoded = io.StringIO(change['owner'].data.decode('utf-8'))
#         filename = change['owner'].filename
#         print('Uploaded `{}` ({:.2f} kB)'.format(
#             filename, len(decoded.read()) / 2 **10))
#         file_contents = decoded.getvalue()

#     _upload_widget.observe(_cb, names='data')
#     display(_upload_widget)

# _upload()

page = """

 """
         
def calculate_frequencies(file_contents):
    # punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    frequencies = {}
    words = file_contents.lower().split()
    for a in words:
        if a not in uninteresting_words:   
            if a.isalpha():
                if a in frequencies:
                    frequencies[a] += 1
                else:
                    frequencies[a] = 1
        
            
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()




myimage = calculate_frequencies(page)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
