---
title: "Math"
math: true
---

## Richard Rast, Model Theorist

I was a mathematician in Model Theory (which is a kind of Logic, which is a kind of Math, at least the way I do it).  I got my PhD at the University of Maryland, under the advisement of Prof. Chris Laskowski.

I spent seven years doing it, in that time I taught a dozen classes, wrote three papers, a thesis, and a textbook, and gave a fair number of talks. Although life took a different course after I graduated, I still look back on those days with a lot of fondness. Along the way I made some good friends, got married, and realized I was ready to leave. Still, I look back on those days with a lot of fondness.

I have this magpie-like urge to collect all the old information about my life, like if I don't write it down and put it somewhere, it didn't really happen. Maybe it's weird. Maybe a generation ago it would have been a scrapbook or a photo album and been totally normal. But still, I like to look at this list every year or two and see if I can remember how everything worked, see if I can remember giving all these talks, see if I can still understand my own writing (so far, so good).

Totally normal stuff.

### Published Papers

<img src="/images/BruceMath.jpg" alt="Not a picture of Richard Rast" style="float:right; width:254px; height:254px; margin:0px 10px" align="right" title="Yes when is math over I'm hungry and bored" />

My research interest was in the Borel complexity of first-order theories (that is, the isomorphism relation on the space of countable models of such a theory).  This can be understood by analogy: given a set of structures, how difficult must a "general algorithm" be to determine if two structures from that set are isomorphic?  The notion of "Borel reductions" is only a useful way to make that imprecise notion into something precise, but it's a well-behaved notion that lines up well with our intuition. If you're familiar with complexity theory in computer science, even vaguely (something something $O(n)$, $O(n^2)$, $P$ vs $NP$) then you can think of that as the *finite* complexity problem, while my work was on the *infinite* complexity problem.

Yes, it was extremely practical. I was beating off NSA recruiters with a stick.

I wrote two papers on "positive results" in this area; that is, times when we can get some kind of classification. Both of them are integrated into my thesis.

- **The Borel Complexity of Isomorphism for O-Minimal Theories**, *Journal of Symbolic Logic* (June 2017) [arXiv](http://arxiv.org/abs/1408.5876).  With Dave Sahota.

    This classified the Borel complexity of isomorphism for all countable o-minimal theories, based on a few model-theoretic invariants.  If the theory admits a nonsimple type (a concept invented by Laura Mayer), the theory is Borel complete.  Otherwise, its complexity is very low, depending entirely on the number of independent nonisolated 1-types.  Specifically, it's equality on countable sets of reals (if there are uncountably many), or equality on a Polish space with cardinality equal to the number of countable models (if there are only countably many).  This work uses builds on the ideas of Dave Sahota's unpublished 2013 PhD thesis, so to honor that, the paper is to be published as joint work between the two of us.
	
- **The Borel Complexity of Isomorphism for Colored Linear Orders**, *Archive for Mathematical Logic* (May 2017) [arXiv](http://arxiv.org/abs/1504.03037)

    This classified the Borel complexity of isomorphism for all colored linear orders (that is, a linear order with countably many unary predicates added), based on a few model-theoretic invariants.  If the theory admits a non-$\aleph_0$-categorical interval type, the theory is Borel complete.  Otherwise, its complexity is very low, depending entirely on the number of nonisolated 1-types.  Specifically, it's equality on countable sets of reals (if there are uncountably many), or equality on a Polish space with cardinality equal to the number of countable models (if there are only countably many).  We also investigated the number of back-and-forth inequivalent models for such theories, and determined the counts lined up exactly with the associated Borel complexity.  This work builds on Rubin's work on colored linear orders, where he defined self-additivity and proved Vaught's conjecture (among other things) for such theories.

On a slightly different topic, but heavily related, is the following question. To show one thing reduces to another, you basically just write down the map.  This can be very difficult, obviously, but the goal is ultimately as clear as the objects themselves.  But suppose you really *can't* reduce one thing to another.  How on earth do you prove that?

- **A New Notion of Cardinality for Countable First Order Theories**, *Archive of Mathematical Logic* (February 2017) [arXiv](http://arxiv.org/abs/1510.05679).  With Douglas Ulrich (first author) and Chris Laskowski.
	
    The goal of this paper (from my perspective; my co-authors might summarize this differently) is to give new tools to show the *nonexistence* of a Borel reduction, as this is incredibly difficult in general, especially when the isorphism relations of the associated theories are not Borel.  To this end we were able to define a "potential cardinality" of a theory, $\|T\|$, where if $T_1$ is Borel reducible to $T_2$, then $\|T_1\|\leq \|T_2\|$. 	This cardinality is the number of "formally consistent, canonical Scott sentences" which imply $T$; in particular this includes the "Scott sentences" of uncountable models of $T$, as well as (in some cases) sentences which have no models, but which do have models in forcing extensions.  
	
    Surprisingly, $\|T\|$ can often be computed directly, allowing us to give several examples of first-order theories which are not Borel complete but whose isomorphism relations are not Borel.  This can happen for a variety of reasons and, if I may plug my own work, I think the first few sections are pretty readable and definitely worth a look.  This is joint work with Douglas Ulrich and Chris Laskowski; in particular many of the best set-theoretic ideas come from Douglas.

**The Borel Complexity of Isomorphism for Some First Order Theories**, *Thesis*, [pdf](/pdf/mainthesis.pdf).

My thesis contains all the information from the o-minimal paper and the linear orders paper, along with slight extensions of both theorems and a somewhat combined approach to both.  It also includes a reasonably large class of examples, not present in the original papers, which may help the reader to understand why certain cases exist (especially for the o-minimal chapter).  Finally, the introduction chapter is much longer and more in-depth than in either of those papers, and even includes a summary of the tools in the potential cardinality paper.  The exposition is quite different, although I think both approaches are good.  If you're interested, take a look! I think it was some of my best mathematical writing.

### Talks

<img src="/images/BruceWanderer.jpg" alt="Full disclosure: I do not travel with a rabbit." style="float:right; width:254px; height:254px; margin:0px 10px" align="right" title="The best part of traveling is the new kinds of food" />

I also gave a number of talks. If you're not in the math world, you might not know this, but math talks can be kind of weird. In theory you're just explaining your research (or whatever you're talking about) to somebody to wants to learn about it, which incidentally is also the theory behind publishing papers. It's such a nice theory. Look, I made this thing and I'm really proud of it! Who wants to look at it?

It's sort of true, but in practice the median number of people who read a published mathematical paper is zero, even in a decent journal. Math is just so niche, so subdivided, so *difficult* that nobody is going to put the time in unless they think it's going to help with their research, or the paper is so approachable that you can skim it on the way to the next paper and get a good sense of how it works. You'd think, hey, this puts a lot of pressure on the writer to make it clear, so somebody would read it, but for whatever reason this mostly doesn't happen. Probably it's just too hard to cover all the details and still make it easy to read. The talks can cover up for that, sort of advertise for the paper. Makes sense.

But still, a lot of people make these talks like they're just reading the papers out loud. The speakers want to cover every little detail, and the listeners (who are only there because they're at the conference anyway, and they have to go to *something*) are bored, playing with their phones, or openly sleeping, except for the one or two people who are working in the same niche and following along eagerly. This always struck me as dumb, and I tried to make my talks as coherent as possible.

Maybe that's why I didn't get a postdoc? Maybe people really want to be put to sleep in a crowded auditorium.

Anyway, even though it didn't work out professionally, I'm still proud of the work I did. Here's a complete list of all the traveling talks I did, at other institutions or conferences, along with a couple I did at the good old U of MD. Also, those slides. I can't believe how long I spent typing out diagrams in beamer. Maybe I was destined for software after all.

- **The Borel Complexity of Isomorphism for Some First Order Theories**
		
	-	*University of Maryland Logic Seminar*, March 29, 2016 [slides](/pdf/DefenseSlides.pdf)  
		60 minutes, Thesis Defense
	
	This covered my thesis!  Except my thesis is 122 pages long, and this talk had an hour.  So it covered the basics of model theory(!), the basics of Borel reducibility, and my two big theorems (outside of potential cardinality): the characterization of o-minimal theories up to Borel reducibility, and the characterization of colored linear orders up to Borel reducibility.  It was aimed at an interdisciplinary audience, rather than specialists, so if you're curious about my research but don't know any logic, this is a good place to start.
	
- **Potential Cardinality**
		
	-	*Rutgers Model Theory Seminar*, April 11, 2016 [slides 1](/pdf/RastRutgers1.pdf) [slides 2](/pdf/RastRutgers2.pdf)  
		3 hours, Invited Talk
		
	-	*AMS Special Session on Descriptive Set Theory and its Applications* at the University of Utah, April 9-10, 2016 [slides](/pdf/RastUtahTalk.pdf)  
		20 minutes, Invited Talk
		
	-	*Penn State Logic Seminar*, March 22, 2016 [slides](/pdf/PennStateTalkMarch2016.pdf)  
		60 minutes, Invited Talk
		
	-	*CUNY Model Theory Seminar*, March 4, 2016 [slides](/pdf/CUNYTalkMarch2016.pdf)  
		75 minutes, Invited Talk
		
	-	*Notre Dame Logic Seminar*, December 1, 2015 [slides](/pdf/NotreDameTalk.pdf)  
		60 minutes, Invited Talk
	
	The aim of these talks was to motivate and define potential cardinality.  This covered Borel reductions, Scott sentences, and back-and-forth equivalence, in order to properly define potential cardinality.  We described some basic results, then used REF as an extended example to demonstrate how it was able to solve new and interesting problems.
	
	Each talk was slightly different, based on my evolving view of how best to present the material, as well as differences in format between the different events and my expectations of how much detail the listeners would want to hear about each topic.
	
- **The Borel Complexity of Isomorphism for Some Ordered Theories**
		
	-	*Second Vaught's Conjecture Conference* at Berkeley, June 1-5, 2015 [slides](/pdf/VCCSlides.pdf)  
		60 minutes, Invited Talk
	
	This covered the content of the o-minimal and the linear orders paper as a combined theorem and proof (skipping a lot of details so that this is actually possible), as well as hinting at possible generalizations. The conference was about Vaught's conjecture, a famous open problem in model theory, and my work was one of very few recent steps towards a solution of a few special cases. Don't get too excited, though: it was unlikely to lead to a general solution.

- **Linear Orderings and the Complexity of Isomorphism**
		
	-	*University of Maryland Logic Seminar*, April 14, 2015 [slides](/pdf/LinearOrdersComplexitySlides.pdf)  
		75 minutes, Home Talk
	
	This covered the main ideas of the linear order paper (above).  It skipped those technical details which are due to M. Rubin, but went through the intuitive part of the argument in significant detail.  It also includes some possible generalizations and parallels between this case and the o-minimal case, with counterexamples to most of the suggested generalizations.
	
- **Countable Model Theory and the Complexity of Isomorphism**
		
	-	*CUNY Model Theory Seminar*, November 21, 2014 [slides](/pdf/Nov21CMT.pdf)  
		60 minutes, Invited Talk
	
	This was intended as a survey talk on the topic, including motivation, examples of failure of traditional (classification theoretic) methods to handle countable model theory, an introduction to the new (Borel) methods, and some results on o-minimal and omega-stable theories.  It probably covered a bit too much content.

- **Borel Complete O-Minimal Theories**
		
	-	*ASL North America Meeting*, May 19-22, 2014 [slides](/pdf/BorelCompleteOMinimalSlides.pdf)  
		15 minutes, Contributed Talk
	
	This covers most of the content of the paper with the similar name, but not all, since the work wasn't completely done at that time.

I've also given a few talks for a "general mathematical audience."  Here is my favorite:

- **Model Theory and Polynomials**
		
	-	*Monroe Martin Spotlight on Graduate Research* competition at the University of Maryland, May 8, 2015 [slides](/pdf/SpotlightTalk.pdf)  
		10 minutes, (Gold Medal winning) Contest Talk
	
	The goal of the Monroe Martin / Spotlight Competition is to present an interesting or useful idea, theorem, or application from your field to a general mathematical audience ... and do it in ten minutes.  This talk was on Ax's theorem, stating that injective polynomials from $\mathbb{C}^n$ to itself are also surjective.  The logic proof is elegant, short, understandable by non-logicians, and clever -- it uses compactness and completeness of $\textrm{ACF}_p$ to prove statements about $\mathbb{C}$ using the pigeonhole principle on finite fields!  This won a Gold Medal in the competition, meaning a jury of my peers (which had only one logician on it) also found it pretty interesting and approachable.

### Awards and Honors

<img src="/images/BruceLook.jpg" alt="Not a picture of Richard Rast" style="float:right; width:254px; margin:0px 10px" align="right" title="Yes is there something you want to give me?" />

I mean, who cares. But I won them, and if I don't write them down, it's like they never happened. Right? Anyway, this is my scrapbook, and looking back on these things makes me nostalgic.

- **Aziz/Osborn Gold Medal in Teaching Excellence, 2010 and 2015**
	
	This is a student nominated award for teaching, given to three winners per year. Funny story about this; 2010 was the first year I was eligible for it, and you're only allowed to win it every five years, which is to say, I won it every time I was eligible to win it. So I'm not saying I *would* have won it every year, and was the greatest teacher in the department forever, but strictly speaking, there's no data to contradict that.

- **Spotlight on Graduate Research (winning talk), 2015**
	
	This is a peer-nominated award for best expository "lightning" talk. It was an actual competition -- dozens of us gave talks on things we knew about that would interest other grad students -- and a jury of our peers picked a couple of winners. I was surprised to win, as there were quite a few good entries, but I think my talk was cool, and everybody was delighted to learn that logic was capable of talking about something outside of logic. It was a good time.

- **James C. Alexanger Prize for Graduate Research, 2016**

	This had a small cash prize (or, for a grad student, a moderate cash prize) but I'm not clear on what metric was used to pick a winner. Not that I'm complaining. This was given at the time my thesis was completed, and was advisor-nominated (thanks!).

- **Mark E. Lachtman Fellowship, 2014**

	This had a small cash prize (or, for a grad student, a moderate cash prize) but I'm not clear on what metric was used to pick a winner. Not that I'm complaining. This was given around the time my thesis was really picking up steam, and came with a reduction in teaching duties for a semester, to encourage me to finish something (it worked!).

