# Vragen aan docenten
-   [ ] Het mag in het Engels... toch?
-   [ ] Ik wil competitie doen:
    -   Hoe werkt dit?
    -   Kan ik er meerdere doen?
    -   Is er iemand die mij kan helpen met de juiste vinden en het invoeren?
-   [ ] Wat voor "profiel" is mijn PWS? Gewoon E&M?
-   [ ] Meedoen met uitleg?


# Research question
**To what extent is perceived enjoyment of the I - V - IV - iv chord progression shared within audiences of American music?** 

## Sub-questions
1.  What is the difference between the relation of perceptual consonance and dissonance throughout a I - V - IV - iv chord progression and the ideal relation of perceptual consonance and dissonance?
2.  To what extent is perceived enjoyment of the I - V - IV - iv chord progression shared upon initial, isolated observation?
3.  What is the relation between the popularity of a song and the use of a I - V - IV - iv chord progression?

### Idea behind
1.  Proving/disproving using physics/math
2.  Proving/disproving using people's general observation / questionnaire
3.  Proving/disproving using a database of songs ranked by popularity and the use of the I - V - IV - iv in those songs.

# Theoretical framework
-   Tenny Height: [mathematical function]: the quantity measures the harmonic complexity of the interval
-   Harmonic ratio
-   Partial
-   (perceived) Consonance
-   (perceived) Dissonance
-   Harmonic complexity: amount of dissonance
-   Chord progression
-   Triad
-   Interval
-   Perceived enjoyment
    -   Enjoyment comes from the expectation of dissonance, and the resolution of dissonance using consonance.
-   American society        
    

# Methodology
## Question 1
-   Measure dissonance using Tenney Height
    -   First, express intervals as just ratios.
    -   The Tenney norm of any frequency ratio $\frac{n}{d}$ is given by $\log_2(nd)$. 
    -   The total dissonance of a triad is given by $TH(\text{lower interval}) + TH(\text{middle interval}) + TH(\text{upper interval})$
[NIET AF]

# Layout
## Question 1
-   Introduce the subject. 
    -   Define a well-established notion: enjoyment comes from a build up of dissonance, and the resolution of dissonance using consonance.
    -   Build on this notion using the Wundt curve: $w(x) = 4x(1 - x)$ and gives us an "ideal build up and resolution of dissonance".
    -   Include pictures of a piano octave with two keys (deriving from the triads to be analyzed) selected, and their accompanying isolated partial note sound waves. Then accompany those visuals with the raw sound using [sound in latex tool]. Express the total amount of dissonance in these intervals using Tenny Height. 
-   Use the previously established foundation to analyze the chord progression, using the same structure, but with the four triads. For each triad: piano octave with three selected notes, three partial sound waves in a graph, and raw sound. Express the total amount of dissonance in these triads using Tenny Height.
-   Normalize the values of dissonance of the four chords throughout the chord progression to a domain of $x \in [0, 1]$ where x = 0 yields dissonance at the start of the progression and $x = 1$ yields dissonance at the end of the progression, and $y = 100\%$ defines "maximum dissonance", which is defined by the most dissonant chord in the chord progression.
-   Plot the values of dissonance as a function
    -   [potential method 1] For each of the four values, draw a dot on a graph. Draw straight lines connecting those dots.
    -   [potential method 2] For each of the four values, draw a straight line covering the amount of time the chord plays.
-   and define a numerical table 
    -   For every x = chord, x = a fourth
    -   For each chord x, show the value y of dissonance
-   Compare the function of the chord progression that of the windt curve. 
    -   Geometrically, this is done by simply graphing the wundt curve over the chord progression. 
    -   Numerically, this is done by comparing the two values using MSE
-   The amount of difference between the two graphs is analyzed using max. vcp

## Question 2
-   Establish a population
    -   Acknowledge location bias
    -   Western Society *can* be researched if the following is considered
        -   The survey will be taken in a quiet classroom in school & online using SurveyCircle
        -   The survey will be made digitally [using what application?], but — in physical survey taking — a physical backup will be kept (with local audio fragments on a digital device)
        -   Every participant must be a resident of a country that reaches the threshold of a share of more than 10% of American artists in their national charts. This can be found [here](https://www.skoove.com/blog/spotify-local-vs-global-music/)
        -   After the survey has been done, the margin of error is decided by evaluating the final sample size (95% betrouwbaarheidsinterval met margin of error als variable en steekproef en populatie als constanten)
-   Establish the research questions (10 questions)
    -   Population check (1 question): Please list all the countries in which you have been a resident for more than 1 year.
    -   Golden questions (3 questions): Isolated audio fragments of the I - V - IV - iv chord progression. Expressed through pure sine waves, played at varying speeds and pitches to avoid confounding variables. The respondent gives their perceived "enjoyment" on a scale of 1-10.
    -   Relativity questions (6 questions): isolated audio fragments of other chord progressions. These control progressions were selected from frequently occuring four-chord progression in American music
        -   
        -   
        -   
        -   
        -   
        -   
        Played at varying speeds and pitches to avoid confounding variables. The respondent gives their perceived "enjoyment" on a scale of 1-10.
    -   

## Question 3
-   A list will be made of 
    


# foreword
have you ever heard an instrumental that made you emotional? well, if you did, i'm willing to bet that it contained an i - iv chord progression.

or, at least, that's what I've noticed about my own music taste.

# Sources
(https://www.researchgate.net/figure/Number-of-frequent-chord-progression-patterns-as-a-function-of-the-chord-progression_fig2_278677700)