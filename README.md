## Bloody (S)hell
---

Bloodyshell is a ground up rebuild of [basicRAT](https://github.com/vesche/basicRAT) with many design changes.
BasicRAT has a few problems that are difficult to address. the critical parts of the code change too frequently, 
and has undergone so many design changes, that it feels clunky, and hard to manage. Bloodyshell is a way back to the roots.
The core idea without all the fancyness involved. maybe if the core features and things that are broken in basicRAT 
are implemented the right way from the beginning, everything else will fit into place. This also allows me to try some of my design ideas.
Being a collaborative project which, while I'm a main contributor, is not mine, means that all of my ideas are discussed with [vesche](https://github.com/vesche/), and some are shot down.
Others are liked and I get the greenlight to try them. But ultimately the complicated code base prevents me from doing so. 
This is a place where all of those ideas can be tested, changed, added, removed, and pondered in a relatively young codebase. 
Some of my better ideas/fixes will make their way into basicRAT, which should still be considered the main attraction.

If you want a more complete RAT with more features, crypto, and everything your heart desires, then use basicRAT. It's not perfect.
But It's pretty alright. If you want an in-development RAT thats easy(ish) to read, works maybe sometimes and is merely a playground... 
Well, you can probably still find something more suitable, but this will do the trick. Aspiring malware authors, Pull requests are very welcome.


### FAQs 
##### (im assuming. Nobody has even seen bloodyshell yet.)
---
 #### Where is the server? Theres a client, but no server?!?!?
 Currently, yes, there is no server. Actually there is but it's terrible and not worth publishing currently.
 For testing, and hell even C2, use `nc -lp 1337`.
 
 #### What is XXX part of the code? it seems entirely useless.
 It probably is. this is a prototype. some code may be unnessarily abstracted or just pointless. It's likely a placeholder.
 
 #### Will this become the new basicRAT?
 probably not. It's likely just going to be a place where I can try new features, debug them and get them ready for integration into basicRAT.
 
### Contributors
[deadPix3l](https://github.com/deadPix3l)
[vesche](https://github.com/vesche/) - For all the basicRAT code

Disclaimer: 
This RAT is for research purposes only, and should only be used on authorized systems. 
Accessing a computer system or network without authorization or explicit permission is illegal.
The author is not responsible for any use or misuse of this software. 
 