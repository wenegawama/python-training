import string

texto = '''Lord Almighty
I feel my temperature rising
Higher higher
It's burning through to my soul

Girl, girl, girl
You gonna set me on fire
My brain is flaming
I don't know which way to go

Your kisses lift me higher
Like the sweet song of a choir
You light my morning sky
With burning love

Ooh, ooh, ooh
I feel my temperature rising
Help me, I'm flaming
I must be a hundred and nine
Burning, burning, burning
And nothing can cool me
I just might turn to smoke
But I feel fine

Cause your kisses lift me higher
Like a sweet song of a choir
And you light my morning sky
With burning love

It's coming closer
The flames are now lickin' my body
Please won't you help me
I feel like I'm slipping away
It's hard to breath
And my chest is a-heaving

Lord Almighty
I'm burning a hole where I lay

Cause your kisses lift me higher
Like the sweet song of a choir
You light my morning sky
With burning love

With burning love
Ah, ah, burning love
I'm just a hunk
A hunk of burning love
Just a hunk, a hunk of burning love
Just a hunk, a hunk of burning love
Just a hunk, a hunk of burning love
Just a hunk, a hunk of burning love
Just a hunk, a hunk of burning love'''

result = sum([i.strip(string.punctuation).isalpha() for i in texto.split()])

print("There are " + str(result) + " words.")


x = "aaa"
y = "bbb"

 
h = y[:2] + x[2:]

i = x[:2] + y[:2]
print(h,i)