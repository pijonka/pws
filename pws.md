# Vragen aan docenten
-   Popularity formula review

# Research question
**To what extent is perceived enjoyment of the I - V - IV - iv chord progression shared within audiences exposed to American music?** 

## Sub-questions
1.  What is the difference between the average amount of dissonance throughout a I - V - IV - iv chord progression, and the average amount of dissonance in the Wundt curve?
2.  To what extent is perceived enjoyment of the I - V - IV - iv chord progression shared upon initial, isolated observation?
3.  What is the relation between the popularity of a song and the use of a I - V - IV - iv chord progression?

### Idea behind
1.  Proving/disproving using physics/math
2.  Proving/disproving using people's general observation / questionnaire
3.  Proving/disproving using a database of songs ranked by popularity and the use of the I - V - IV - iv in those songs.

# Theoretical framework
-   (perceived) Consonance
-   (perceived) Dissonance
-   Harmonic complexity: amount of dissonance
-   Chord progression
-   Triad
-   Interval
-   Perceived enjoyment
    -   Enjoyment comes from the expectation of dissonance, and the resolution of dissonance using consonance.
-   Audiences exposed to American music
    -   Threshold of [x] percent of American artists in their national charts
    (-   Every participant must be a resident of a country that reaches the threshold of a share of more than 10% of American artists in their national charts. This can be found [here](https://www.skoove.com/blog/spotify-local-vs-global-music/))

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
    -   The Wundt curve: a supposedly "ideal" relation of consonance and dissonance in a song
    -   Include pictures of a piano octave with two keys (deriving from the triads to be analyzed) selected, and their accompanying isolated partial note sound waves. Then accompany those visuals with the raw sound using [sound in latex tool]. Express the total amount of dissonance in these intervals using Tenny Height. 
-   Use the previously established foundation to analyze the chord progression, using the same structure, but with the four triads. For each triad: piano octave with three selected notes, three partial sound waves in a graph, and raw sound. Express the total amount of dissonance in these triads using Tenny Height.
-   Define a "maximum amount of dissonance" in a triad, by measuring the total amount of dissonance in three adjacent semitones in Tenny Height
-   Graph the function of the Wundt curve, but normalize it such that the minimum of the grpah is 0, and the maximum of the graph is the "maximum amount of dissonance"
-   Gather the data into a table with columns "fraction of full chord progression's length in time" [ <-- awfully wordy and inconspicuous], "dissonance in chord progression", and "dissonance in Wundt curve"
-   Compare the data of the table
    -   Geometrically, this is done by placing dots of the chord progression's data over the Wundt curve
    -   Numerically, this is done by comparing the two values using max. vcp
-   This will yield [some kind of relative significant difference]

## Question 2
-   A survey will be taken in a quiet classroom in school & online using SurveyCircle
-   Define a sample and population
    -   Acknowledge location bias
    -   "Audiences exposed to American music" sets the scope to both North American and European citizens, which is a viable sample group for the survey to reach.
    -   Every participant must be a resident of a country that reaches the threshold of a share of more than 10% of American artists in their national charts. This can be found [here](https://www.skoove.com/blog/spotify-local-vs-global-music/)
-   The survey will be made digitally [using what application?], but — in physical survey taking — a physical backup will be kept (with local audio fragments on a digital device)
-   The survey will be written in English and Dutch
-   Establish the research questions (10 questions)
    -   Population check: Please verify that you have resided in any of the countries listed for at least 1 year. Countries that respondents are most likely to be a citizen of are listed in bold:
        -   Netherlands
        -   United States
    -   Golden questions (3 questions): Isolated audio fragments of the I - V - IV - iv chord progression, repeated. Expressed through pure sine waves, played at varying speeds and pitches to avoid confounding variables. The respondent gives their perceived "enjoyment" on a scale of 1-10.
    -   Control questions (6 questions): isolated audio fragments of other chord progressions. These control progressions were selected from frequently occuring four-chord progression in American music
        -   "good sounding chords", or very consonant 
            -   I - V - IV - IV
            -   I - I (+ 1 octave) - I - I (+ 1 octave)
            -   
        -   "bad sounding chords", or very dissonant
            -   
            -   
            -   
            -   
        Played at varying speeds and pitches to avoid confounding variables. The respondent gives their perceived "enjoyment" on a scale of 1-10.
-   One of the respondents of the survey is "Steve ..." from Marillion. Seeing as he is a popular musician, we can assume he has a strong intuition in perceived enjoyment of melodies. He will thus get a customized survey:
    -   For every audio fragment, he will answer what he expects the "overall enjoyment of this audio fragment" of other people to be. He will also reason why he ranked his answer as such
    -   His closed answers will be entered into the database [but will weigh more... maybe?]
-   The results 
    -   Using the following data:
        -   The margin of error
            -   decided by evaluating the final sample size (95% betrouwbaarheidsinterval met margin of error als variable en steekproef en populatie als constanten)
        -   Average amt of enjoyment
        -   Stdev of enjoyment
    -   A 95% betrouwbaarheidsinterval will be opgesteld.
    -   The values will also be listed in a table numerically
-   A conclusion will be made

## Question 3
-   For music from the 20th century The McGill Billboard Corpus dataset will be used to obtain both "chord" and "popularity" data for songs in the 20th century
-   For music from the 21st century, an API given by Hooktheory.com can be used to obtain "chord" data, and a dataset of the Billboard Hot 100 [where the hell did I find this] will be used to obtain "popularity" data
-   Both the aforementioned datasets will be used to the maximum possible extent, with as many entries as possible
-   Popularity will be measured as such:            
    (100 - peak_rank) * weeks_on_chart
-   Once a "song", "popularity", and "use of progression" table can be defined, it will be viewed in these two ways:
    -   2 dimensional dotplot, with the x axis being NUMBER OF USES OF CHORD PROGRESSION and the y axis being popularity
    -   2 box plots [of trust intervals ?], one of average popularity of songs with the chord progression, compared to without
-   The boxplots, specifically, can be compared [in what way? Refer to havo boeken] to define the significance between the two

# discussion (current, not for final research paper)
-   Why is the Wundt curve the "ideal relation of perceptual consonance and dissonance"?

# foreword
Have you ever heard an instrumental that made you emotional? well, if you did, i'm willing to bet that it contained an i - iv chord progression.

or, at least, that's what I've noticed about my own music taste.

# Sources
(https://www.researchgate.net/figure/Number-of-frequent-chord-progression-patterns-as-a-function-of-the-chord-progression_fig2_278677700)
https://www.hooktheory.com/theorytab/view/olivia-rodrigo/stupid-song