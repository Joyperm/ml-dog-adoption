#Groping color columns
def categorize_color(color):
    # Check for 'Monochrome' colors - WHITE, BLACK, or GRAY (independent of other words)
    if any(c in color for c in ['WHITE','BLACK', 'GRAY']):
        return 'Monochrome'
    
    # Check for 'Brown' colors - BUFF, CHOCOLATE, TAN, CREAM, YELLOW
    elif any(c in color for c in ['BUFF', 'CHOCOLATE', 'TAN', 'CREAM', 'YELLOW','BROWN','FAWN']):
        return 'Brown'
    
    # Check for '/' in color, indicating mixed or patterned colors
    elif '/' in color or ' ' in color or 'TRICOLOR' in color:
        return 'Brindle/Patterned/Tricolor'
    
    # If none of the above, classified as 'Other'
    else:
        return 'Other'


# function to display class label
def display_classLabel(y_pred_):
    # Ensure y_pred_ is a single integer, not an array
    label = ''
    if y_pred_ == 0:
        label = 'ADOPTION'
    elif y_pred_ == 1:
        label = 'OTHER'
    elif y_pred_ == 2:
        label = 'RETURN TO OWNER'
    else:
        label = 'TRANSFER'
    
    print('Predicted class membership for the dog is ',y_pred_,', which means ',label)


# function to display predicted probability
def display_PredProb(y_pred_, pred_prob):
    # Determine the class label and extract the probability based on y_pred_
    if y_pred_ == 0:
        prob_label = "The probability of adoption is"
        prob = pred_prob[0][0]  
    elif y_pred_ == 1:
        prob_label = "The probability of other is"
        prob = pred_prob[0][1]  
    elif y_pred_ == 2:
        prob_label = "The probability of return to owner is"
        prob = pred_prob[0][2]  
    else:
        prob_label = "The probability of transfer is"
        prob = pred_prob[0][3]  

    print(f'Predicted probability for the dog is {prob:.2f}. {prob_label} {prob:.2f}')
