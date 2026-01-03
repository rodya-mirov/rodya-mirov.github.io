---
title: "Hobby Programming"
---

## Richard Rast, Hobbyist Programmer

<img src="/images/BruceIT.jpg" alt="Not a picture of Richard Rast" style="float:right; width:254px; height:254px; margin:0px 10px" align="right" title="This doesn't seem so hard" />

I started programming in middle school, writing TI-BASIC on a TI-83+ calculator. I wanted to automate some extremely repetitive geometry homework problems, which worked. Then I made some "cool graphs." But one day -- I think it was in high school -- I found the `INPUT` command, which could take arbitrary strings from the user, and found I could stick it in if-statements, add it to other strings, the works. Then something clicked in my brain. This thing was _powerful_. This could do _anything_.

That feeling has never really left.

Most of my programming nowadays is at work, and it's closed source and trade secrets and whatever, but sometimes, if I have time and an idea worth the trouble, I do a little on the side. Here's a nonexhaustive sampling, in reverse chronological order. Most of these things weren't ever intended to be finished.



### Programming Languages

I've been interested in programming languages for years. Not sure why; I guess it feels like the computer science version of my PhD research. But I think they're beautiful. Plus, a clean slate lets you pretend all the nastiness of [that language you hate] can be wiped away with no downside, just the experience of hindsight.

If you want to keep that feeling, try not to finish anything. Here's my scrapbook!

- **longleaf** [(repo)](https://github.com/rodya-mirov/longleaf) -- circa 2022

    This was a good one. The idea was to compete with numpy/matlab, on the idea (which might have been a little naive) that most people wanted "simple" matrix operations that ran very efficiently and very quickly, rather than huge standard libraries of pretty-good performance. The big innovations were using rust/rayon for parallelism, and reusing vectors after they're released to reduce re-allocation churn.

    The benchmarks were impressive, and they did indeed outperform numpy, but in hindsight it's obvious that people were and are more interested in a big library and ecosystem than in getting 2-3x speedups on simple matrix algebra. Still, though!

- **bf** [(repo)](https://github.com/rodya-mirov/bf) -- circa 2020

    This was an optimizing brainfuck compiler (!), inspired by an advent of code problem I took much too seriously. I didn't know it at the time, but optimizing BF compilers are a bit of a sport within a certain community, because BF code is begging for it (e.g.: to add two consecutive registers, you run `[->+<]`, which is actually a loop that moves value, one at a time, from the left register to the right).

    So the idea here was to find some interesting BF programs on the internet (which is hard enough), observe that they naturally run _very slowly_, then write an optimizer until they run fast. It was a lot of fun!

- **burstlang** [(repo)](https://github.com/rodya-mirov/burstlang) -- circa 2019

    My first effort to write programming language in rust, and my first exposure to bytecode. The focus was on testability and learning the fundamentals.

- **Brucelang** [(repo)](https://github.com/rodya-mirov/Brucelang) -- circa 2018

    This is an actual new programming language, implemented in Java. The idea was fairly interesting, and at the time I had some delusions of grandeur that told me this was really going to be something. The idea was to build an interpreter that you would hook into your actual program (sort of how Lua hooks into video games) and feed data into it.

    The twist was this isn't Turing complete, but it was _useful_. As a consequence of that simplicity, you could do things like examine code _before running it_ and tell how long it was going to take to run, as a function of the input. You could also prove certain invariants were preserved.

    The intention was to be able to allow untrusted input which would both ensure PII didn't leak, and to ensure that their code would stay within the resource confines we wanted to grant them.
    
    I still believe it could work, but the associated work project was canceled, and at a certain point it didn't make sense to keep working on this. But I'm proud of it, and I would love to go back and work on it if there was a need. I've since found out that others have had this idea, too, and it's of interest in the academic programming language world, so that's a fun little validation.

- **Robodorf** [(repo)](https://github.com/rodya-mirov/robodorf) -- circa 2016

    This was a Pascal interpreter written in Java. Not because I care about or even know Pascal, but because there was a blog post series about it, and I was intrigued. This went a bit farther than the blogs I was following, adding type checking and a lot of tests, but beyond that it was a pretty simple tutorial following. Still, it was a lot of fun and I learned a lot, and it set the seeds for things that came later.



### Twisty Puzzles

I got into Rubik's Cubes during the pandemic, as a way to keep off my phone during lockdown. But then lockdown ended and I just kept buying these things. I've got north of eighty at this point.

They're interesting to solve, and kind of meditative once you get the knack of it, but there's also some interesting math there. For instance -- how many configurations can you get a Rubik's cube into? How many moves do you absolutely _need_ to solve one? Well we know the answer for the regular cube, but how about the 2x2? The 4x4, or the 5x5? The pyraminx? The hanoi war drums puzzle?

Look, there's a lot here.

I wrote some general purpose code to solve this stuff, at least for the smaller puzzles [(repo)](https://github.com/rodya-mirov/twisty), which handles about a dozen of them at this point. It can generate fair scrambles for most of them, solve a given scramble, and (in the smaller cases) compute the graph diameter and number of configurations. It's not cutting edge, nothing like what Kociemba did, but it was a good little side project.

I also wrote some blog posts about how the math works [(see blog)](https://rodyamirov.wordpress.com/) which work together with the repo. See for instance [(this one)](https://rodyamirov.wordpress.com/2023/12/27/twisty-puzzles-the-2x2x3/) which talks about how you can turn a dinosaur into a Cronenbergian monstrosity in 14 moves or less.



### Game Development

Even before I ever got a software job, I was trying to make video games on the side, although it was just for fun and nothing ever went to market. This was before Steam was fully open, anyway, and before itch.io and serious games in the browser, and going to market was a high bar.

Software rots very quickly, and games more than most -- I suspect less than half can be compiled easily. Still, it's fun to look back over them.

- **Radishes** [(repo)](https://github.com/rodya-mirov/radishes) -- circa 2019

    Another tower defense, but _in rust_, and _in the browser_. This one still compiles and works (if you update wasm-bindgen)! It's a little barebones, but that was a delightful little blast from the past.

- **Palladium** [(repo)](https://github.com/rodya-mirov/palladium) -- circa 2018

    This one was pretty cool. It's a roguelike, sort of, in the browser. It had a nontrivial physics system, getting into ECS and so on, and it had a cool timeloop mechanic, where you're on a space station and trying to figure out what's going on, but each time you die, you come back to the start.

    It was original at the time, okay? There were plans for using it for storytelling (you could learn something about someone on one loop, then use that information on subsequent loops) but this never got past the engine phase. Also, sadly, bitrot has made it very difficult to run this program.
	
- **Voxelist** [(repo)](https://github.com/rodya-mirov/Voxelist) -- circa 2013
		
    This was like a 3D version of Infinite Tile Engine 2D, but I knew going in that I was only interested in the engine.  It has support for "infinite" 3D procedurally generated worlds, and the ability to walk around that world in first person.  The demo projects use some hand-made maps and some maps that use value noise and splines to generate the terrain, along with some graphics that I spent too much time drawing.

    Even then XNA was "over," but was still useable and even supported (to an extent). Unfortunately, you'd have trouble compiling it at this point. If you'd like to use the source code or play with the games, you'd have to port it to [Monogame](http://www.monogame.net/).  Fortunately, and very unlike the situation in 2012, Monogame is a mature enough platform that this is a fairly straightforward process.

- **Infinite Tile Engine 2D** [(repo)](https://github.com/rodya-mirov/Infinite-Tile-Engine-2D) -- circa 2012
		
    This is the underlying engine for what was intended to be (but never became) a [Dwarf Fortress](http://www.bay12games.com/dwarves/) clone.  Yes, that's the best and worst game that's every been made, and yes, like every other hobbyist game programmer, I wanted to be the guy that made "Dwarf Fortress, but playable."  No, it can't be done, and yes, it [has been done](http://gnomoria.com/).  The successes and failures of Gnomoria should be lesson enough, but there will always be proud men who want to unseat their betters.
		
    More usefully described, this project contains enough information for a procedurally generated (2D) world, in an isometric perspective.  It has support for tilesets, player constructions, function-based landscape, and NPCs (to some degree).  I tried making some games with it; this project was developed simultaneously with *Cow Mouse*, which was the actual "game" (although see above).
	
- **Frog Defense** [(repo)](https://github.com/rodya-mirov/Frog-Defense) -- circa 2012
		
    This is a tower defense game *with a twist* -- instead of building towers along a preordained path, you are given a start and end portal, and you have to dig out the path that the monsters go along.  You have to choose between making more guns or making a longer path (they both cost money), and the balance was I think pretty good.  The art was by yours truly, so it's pretty bad.  It's a complete game, though!  This was made as part of an unofficial 7 Day Game Development Challenge.

- **Picross** [(repo)](https://github.com/rodya-mirov/Picross) -- circa 2012

Farther back than that, you'd have to go find my old TI-83+ calculator and look at whatever code is still on there. Miraculously it still works, although the screen has significant damage, and you can play tetris (not mine). But all my original code is lost in time, like tears in the rain.



### Puzzle Sites

I love the Advent of Code. I haven't finished every year, and certainly never bothered with the leaderboards, but I've done a lot of them, and I always look forward to them.

- **2025** [(repo)](https://github.com/rodya-mirov/aoc_2025)
  
    2025 was a fun one, right? Just 12 days this year. The first seven days were so trivial, then BAM. Casuals go home. Full disclosure, I didn't do integer programming on Day 9, but I did spend a couple hours sitting with my wife row reducing matrices (mathematician marriages have funny outcomes) and even then, the idea for how to use the null-space occurred to me a few days later while I was at the gym. Really good year.

    Then day 12, right? Throw an NP-complete problem in there. I solved it by complete luck, and I consider my solution to be a bit of a cheat, and I intend to go back and solve it for real "someday" but someday hasn't come yet.

- **Older years**

    I did a bunch of them, to greater or lesser extent. I got all 50 stars in 2022 [(repo)](https://github.com/rodya-mirov/aoc_2022) and 2017 [(repo)](https://github.com/rodya-mirov/aoc_2017) (woo! Turing Machines!) and 47 stars in 2021 [(repo)](https://github.com/rodya-mirov/aoc_2021) (I really want to go back and do day 24 at some point), and after that it kind of trails off. Still, I love it.

I've also done a bunch of project euler problems, but you're not supposed to share your solutions (which doesn't stop anybody, but like, it feels funny putting it on your website). The first hundred or so are a lot of fun, before they get totally weird or obsessively niche mathematics (and not in my niche, sadly).
