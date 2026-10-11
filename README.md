# PWS research project: "To what extent is perceived enjoyment of the I - V - IV - iv chord progression shared within audiences exposed to American music?"

## Overview
This research project aims to be a case study for a bigger question I've been wondering about all my life: **is music objective to some extent?** To produce an accurate result while realistically considering the resources of the project, it deliberately limits its scope to one chord progression (I - V - IV - iv) and one audience (those exposed to American music).

To find that extent of objectivity in the chord progression, I built on external findings about **harmonic complexity** and the **Wundt Curve**. These suggest that perceived enjoyment in terms of complexity have an inverted U shaped relation, and that the vertex of this curve lies at a moderate amount of complexity. Using **Python scripts for calculations and data collection** (including an automated analysis of **~800 songs**), and **surveys for more data collection**, I produced results that are not only in line with external findings so far, but also map the harmonic complexity of chord progressions in such a way that we can see where they lie on this curve. 

My research so far suggests that the average normalized harmonic complexity of the I - V - IV - iv chord progression, ~45%, is close to the vertex of this curve, which is confirmed by the fact that its perceived enjoyment is highly shared among people.

## Subquestion 1: "How does the average normalized harmonic complexity of the I - V - IV - iv chord progression compare to different chord progressions?"

### Methodology
To start, *normalized harmonic complexity* was defined as a scale of 0-100% harmonic complexity, where 0% is a double octave, and 100% is a triad of adjacent notes. Pure harmonic complexity was measured through Just Intonation ratios and the Tenney Height function, and those values were used to define those 0% and 100% bounds.

The average normalized harmonic complexity was calculated by creating an array for each chord progression with each value being the harmonic complexity of either a major or minor chord, calculating the mean of that array, and normalizing that amount of harmonic complexity.

### Results
The normalized harmonic complexity of the I - V - IV - iv chord progression turned out to be ~45%, while chord progressions with more/less minor chords deviated from this spot, revealing an interesting middle position relative to other chord progressions.

## Subquestion 2: "To what extent is perceived enjoyment of the I - V - IV - iv chord progression shared upon initial, isolated observation?"

### Methodology
A survey was held online and filled in by ~30 people. The survey prompted respondents to listen to audio fragments of a variety of chord progressions (played on a piano) and rate their enjoyment. The survey also collected demographic data from respondents. 

### Results
The results revealed that the I - V - IV - iv chord progression sits at a high value of perceived enjoyment compared to the other chord progressions, though not uniquely high; chord progressions with a similar amount of minor chords sit at this same value, or an even higher value.


## Subquestion 3: "What is the relation between the popularity of a song and the use of a I - V - IV - iv chord progression?"

### Methodology
The McGill Billboard Corpus dataset was used for both chord and popularity data.

Two Python modules were created for the parsing and analyzing of chord data. The parser parsed unstructured strings into lists of chords. The analyzer analyzed a list of chord data, such that uses of a chord progression (including those with repetitions of one chord) would be counted. (These modules are currently available to view/download in the data/q3 directory, but will soon be polished and posted as submodules for other projects.)

Popularity data was found using a simple formula using the variables "peak_rank" and "weeks_on_chart" from the dataset.

The Python modules were put together in one script to iterate and extract data from the McGill Billboard Corpus dataset. The analyzer module was instructed to find variations of the I - V - IV - iv chord progression.

### Results
Unfortunately, the McGill dataset did not contain enough uses of the I - V - IV - iv chord progression to signify any relation between popularity and the chord.

## Current status