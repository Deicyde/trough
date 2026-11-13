# Weyl

The folder [Physlib/Relativity/Fermions/Weyl/](https://github.com/leanprover-community/physlib/tree/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl): 9 modules, an article each, in path order with Basic.lean first in its folder.

The repository's API map for this folder, *Weyl Fermions* ([Physlib/Relativity/Fermions/Weyl/API-map.md](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/API-map.md)), with the sentences it marks as not yet formalized left out (…). A citation \[n\] links the module its n-th Lean reference names.

*Content (Alpha)*

> ### The four spinor spaces
>
> A left-handed Weyl spinor ψ\_α is an element of a two-dimensional complex vector space. [\[1\]](lefthanded.md) A right-handed Weyl spinor ψ^\{α̇} is likewise an element of a two-dimensional complex vector space. [\[2\]](righthanded.md) Each has a dual, ψ^α and ψ\_\{α̇}, again a complex vector space. [\[3\]](duallefthanded.md)[\[4\]](dualrighthanded.md) Each of the four spaces has a two-element basis, and every spinor expands in it. [\[5\]](lefthanded.md)[\[6\]](righthanded.md)[\[7\]](duallefthanded.md)[\[8\]](dualrighthanded.md) Each carries a representation of SL(2, ℂ), the double cover of the restricted Lorentz group \{1}, whose matrix in that basis is the defining matrix, its conjugate, its inverse transpose or its inverse conjugate transpose as appropriate. [\[9\]](lefthanded.md)[\[10\]](righthanded.md)[\[11\]](duallefthanded.md)[\[12\]](dualrighthanded.md) Each of these representations is irreducible, and Schur's lemma holds for it: an endomorphism commuting with the representation is a scalar multiple of the identity. [\[23\]](lefthanded.md)[\[24\]](righthanded.md)[\[25\]](duallefthanded.md)[\[26\]](dualrighthanded.md) Weyl fermions are the building blocks of Dirac fermions \{2}, and the two-component formalism follows Dreiner, Haber and Martin \{3}.
>
> ### Contractions, metrics and units
>
> Each Weyl type pairs invariantly with its dual, giving bilinear maps that are also intertwining maps of representations. [\[13\]](contraction.md) On basis elements these contractions are Kronecker deltas, and each is symmetric under exchanging its two factors. [\[14\]](contraction.md)
>
> The epsilon metrics ε\_\{αβ}, ε^\{αβ}, ε\_\{α̇β̇} and ε^\{α̇β̇} are invariant tensors, intertwining maps out of the trivial representation, with explicit expansions in the basis. [\[15\]](metric.md) Their invariance rests on the raw epsilon matrix ε intertwining M ∈ SL(2, ℂ) with its inverse transpose, Mε = ε(M⁻¹)ᵀ, and the complex conjugate of M with its inverse conjugate transpose. [\[16\]](metric.md) Contracting a metric with the metric of the dual type over one index gives the unit, ε\_\{αβ}ε^\{βγ} = δ\_α^γ, and likewise for the other types. [\[17\]](metric.md)
>
> The units δ\_α^β and δ^\{α̇}\_\{β̇} realize the duality between each type and its dual, and contracting a unit with a spinor returns that spinor. [\[18\]](unit.md) Each unit is symmetric under exchange of its two factors. [\[19\]](unit.md)
>
> ### Duality and matrices
>
> The dual of the left-handed representation is the representation on the dual left-handed spinors. [\[20\]](duals.md) … Pairwise tensor products of the Weyl types are 2 × 2 complex matrices, equivariantly for the action of SL(2, ℂ). [\[21\]](two.md) …

Its references:

> - \{1\} Lorentz Group API map — [Physlib/Relativity/LorentzGroup/API-map.md](../../lorentzgroup/README.md)
> - \{2\} Dirac Fermions API map — [Physlib/Relativity/Fermions/Dirac/API-map.md](../dirac/README.md)
> - \{3\} H. K. Dreiner, H. E. Haber and S. P. Martin, *Two-component spinor techniques and Feynman rules for quantum field theory and supersymmetry*, Phys. Rept. 494 (2010) 1–196, arXiv:0812.1594, https://arxiv.org/abs/0812.1594.

- [Contraction of Weyl fermions](contraction.md)
- [Dual left handed Weyl fermions](duallefthanded.md)
- [Dual right handed Weyl fermions](dualrighthanded.md)
- [Duals for fermions](duals.md)
- [Left handed Weyl fermions](lefthanded.md)
- [Metrics of Weyl fermions](metric.md)
- [Right handed Weyl fermions](righthanded.md)
- [Tensor product of two Weyl fermion](two.md)
- [Units of Weyl fermions](unit.md)
