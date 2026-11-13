# GalileanGroup

The folder [Physlib/SpaceAndTime/GalileanGroup/](https://github.com/leanprover-community/physlib/tree/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup): 1 module, an article each, in path order with Basic.lean first in its folder.

The repository's API map for this folder, *Galilean group* ([Physlib/SpaceAndTime/GalileanGroup/API-map.md](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/GalileanGroup/API-map.md)), with the sentences it marks as not yet formalized left out (…). A citation \[n\] links the module its n-th Lean reference names.

*Content (Alpha)*

> A Galilean transformation consists of four pieces of data: a rotation, a boost velocity, a translation of space \{1} and a translation of time \{2}. [\[1\]](basic.md) The spatial dimension is arbitrary; nothing is special to three dimensions. [\[6\]](basic.md)
>
> Galilean transformations form a group, with the identity, the composite and the inverse computed explicitly from the four pieces. [\[2\]](basic.md) …
>
> The Galilean group acts on time and space together: an element sends a pair of an instant and a point to the pair obtained by rotating and boosting the point, then translating both. [\[7\]](basic.md)
>
> The Galilean group is assembled from familiar subgroups, each of which includes into it. The rotations include into the Galilean group, as do the elements of the full orthogonal group. [\[3\]](basic.md) The space translations include into the Galilean group. [\[4\]](basic.md) The time translations include into the Galilean group. [\[5\]](basic.md) More generally, the Euclidean group of space, the transformations combining a rotation and a translation of space, includes into the Galilean group. [\[8\]](basic.md)

Its references:

> - \{1\} Space API map — [Physlib/SpaceAndTime/Space/API-map.md](../space/README.md)
> - \{2\} Time API map — [Physlib/SpaceAndTime/Time/API-map.md](../time/README.md)

- [The Galilean group](basic.md)
