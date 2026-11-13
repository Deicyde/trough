# LorentzGroup

The folder [Physlib/Relativity/LorentzGroup/](https://github.com/leanprover-community/physlib/tree/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup): 11 modules, an article each, in path order with Basic.lean first in its folder.

The repository's API map for this folder, *Lorentz Group* ([Physlib/Relativity/LorentzGroup/API-map.md](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/API-map.md)), with the sentences it marks as not yet formalized left out (…). A citation \[n\] links the module its n-th Lean reference names.

*Content (Alpha)*

> ### The group
>
> A Lorentz transformation is a matrix Λ satisfying Λ * dual Λ = 1, where the dual is taken with respect to the Minkowski matrix. [\[1\]](basic.md) The Lorentz transformations form a group under matrix multiplication. [\[2\]](basic.md) Equivalently, Λ is Lorentz exactly when dual Λ * Λ = 1, when its transpose is Lorentz, when −Λ is Lorentz, or when Λᵀ η Λ = η. [\[6\]](basic.md) The Lorentz group embeds as a closed subgroup of the general linear group, by a closed embedding. [\[3\]](basic.md) … It is the symmetry group of Minkowski spacetime \{1}, and Lorentz tensors \{2}, Weyl fermions \{3} and Dirac fermions \{4} are characterized by how they transform under it. A standard introduction is Jaffe \{5}.
>
> ### Boosts and rotations
>
> Every boost is a Lorentz transformation. [\[4\]](boosts-basic.md) Every rotation of space is a Lorentz transformation. [\[5\]](rotations.md) Every member of the restricted Lorentz group is a boost composed with a rotation. [\[10\]](restricted-fromboostrotation.md)
>
> ### Proper, orthochronous and restricted transformations
>
> A Lorentz transformation is proper when its determinant is 1. [\[7\]](proper.md) It is orthochronous when it preserves the direction of time, its time-time component being non-negative. [\[8\]](orthochronous-basic.md) The restricted Lorentz group consists of the transformations that are both proper and orthochronous. [\[9\]](restricted-basic.md) …

Its references:

> - \{1\} SpaceTime API map — [Physlib/SpaceAndTime/SpaceTime/API-map.md](../../spaceandtime/spacetime/README.md)
> - \{2\} Tensors API map — [Physlib/Relativity/Tensors/API-map.md](../tensors/README.md)
> - \{3\} Weyl Fermions API map — [Physlib/Relativity/Fermions/Weyl/API-map.md](../fermions/weyl/README.md)
> - \{4\} Dirac Fermions API map — [Physlib/Relativity/Fermions/Dirac/API-map.md](../fermions/dirac/README.md)
> - \{5\} A. Jaffe, *Lorentz Transformations, Rotations, and Boosts*, https://cdn.ku.edu.tr/cdn/files/amostafazadeh/phys517\_518/phys517\_2016f/Handouts/A\_Jaffi\_Lorentz\_Group.pdf

- [The Lorentz Group](basic.md)
- [The Proper Lorentz Group](proper.md)
- [Rotations](rotations.md)
- [Vectors from Lorentz group elements](tovector.md)

Modules in [Boosts/](https://github.com/leanprover-community/physlib/tree/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts):

- [Boosts in the Lorentz group](boosts-basic.md)
- [Physlib.Relativity.LorentzGroup.Boosts.Apply](boosts-apply.md)
- [Coordinate-axis boosts in `SL(2,ℂ)` and the Lorentz group](boosts-axis.md)
- [Generalized Boosts](boosts-generalized.md)

Modules in [Orthochronous/](https://github.com/leanprover-community/physlib/tree/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Orthochronous):

- [The Orthochronous Lorentz Group](orthochronous-basic.md)

Modules in [Restricted/](https://github.com/leanprover-community/physlib/tree/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Restricted):

- [The Restricted Lorentz Group](restricted-basic.md)
- [The construction of an element of the Lorentz group from a boost and a rotation](restricted-fromboostrotation.md)
