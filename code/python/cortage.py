def cortegeToSet(cortege):
    l = len(cortege)
    if (l<=0):
        return '\\emptyset'
    strX1=cortege[0]
    strX2XN=cortegeToSet(cortege[1:])
    #return '\\{\\{' + strX1 + '\\},\\{' + strX1 + ',' + strX2XN + '\\}\\}' #LaTeX output
    return '\\{' + '\\{' + strX1 + ',' + strX2XN + '\\}' + ',' + '\\{'  + strX1 + '\\}' + '\\}' #LaTeX output crypt
    #return '{{' + strX1 + '},{' + strX1 + ',' + strX2XN + '}}' #simple output
    
print('\\begin{enumerate}')
print('    \\item ' + '$' + cortegeToSet(['b','a'])         + '$;')
print('    \\item ' + '$' + cortegeToSet(['a','c','b'])     + '$;')
print('    \\item ' + '$' + cortegeToSet(['d','a','c','b']) + '$.')
print('\\end{enumerate}')
