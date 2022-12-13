# CS110 Final Exam

## SHORT DESCRIPTION: An application that recommends concerts based on a given artist

## KNOWN BUGS AND INCOMPLETE PARTS Some artists don't work due their their labeled genre in Deezer not working with SeatGeek's API, so artists defined by a genre with a single word (like rock or pop) should work

## REFERENCES API Documentation for both Deezer, SeatGeek, and the MapQuest and GeoDB APIs as well

## MISCELLANEOUS COMMENTS *(anything else you would like the grader to know)* The Mapquest and GeoDB APIs were used to find the nearest city from the user to search for events, and it was working, but the search ended up being too wonky (its definition of city included counties which messed things up) most times to where no events were found.