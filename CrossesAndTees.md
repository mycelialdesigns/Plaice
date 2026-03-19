# Crosses and Tees

It's common in Plaice for two or more plates to meet at right angles to each other, with some kind of connector between them. In the case
where there are only two plates, corners are used (TODO: link), but in situations where more plates meet, crosses and tees are needed instead.

## Crosses

When four plates meet, a cross connector may be used to hold them together with slide (or glide) connections. 

Glide connections are denoted with two parallel lines engraved onto the top and bottom faces, with the connectors "sandwiched"
between them being the glide connections, and the other connectors assumed to be slides. 

The spacing of slide connectors on a cross are set up to ensure that along each straight, exactly one cell unit (1 CU) is consumed,
which ensures that Plaice plates with crosses maintain alignment with contiguous Plaice plates. 

The chamfers between the four prongs of a cross are interrupted by .25HU straights to allow for flush mounting of Plaice covers.

The intruding and protruding connectors of crosses are set up so as to not reverse the directionality of slide connectors on Plaice plates
connected along the straights of the cross, which enables easier reasoning about plate orientations. 

## Tees

Tees are for when three Plaice plates meet. They are basically crosses with one of the slide connectors removed, with the removed-connector
side given several stub Plaice sockets along the flat. This is done to maintain the continuity of the socket grid across plates connected
along the flat. 

Tees are named after whether their right-angle connection is protruding or intruding, and the clearance level (slide or glide). 
Just like with crosses, "glide" tees are denoted by two parallel lines engraved onto the top and bottom faces. 

### Printability modifications

All tees have a printability modification which adds a thick brim to their outer straight to help prevent the tee from toppling while printing.
