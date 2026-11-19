---
declaration: theorem
origin: cited
lean: Representation.pseudoreflectionSubgroup_eq_top_iff_exists_bijective_aeval_symmetricAlgebraInvariants_dual
statement: formalized
proof: formalized
---

# The Chevalley–Shephard–Todd theorem (`Representation.pseudoreflectionSubgroup_eq_top_iff_exists_bijective_aeval_symmetricAlgebraInvariants_dual`)

Let a finite group `G` act faithfully and linearly on a
finite-dimensional vector space `V` over a field `K` of characteristic zero. Then `G` is generated
by pseudoreflections, the elements whose fixed space is a hyperplane, if and only if the
polynomial invariants `Sym(V*)^G` form a polynomial algebra on homogeneous invariants
`f₁, …, fₙ` of positive degree, where necessarily `n = dim V`.

```lean
Representation.pseudoreflectionSubgroup_eq_top_iff_exists_bijective_aeval_symmetricAlgebraInvariants_dual.{u_1,
    u_2, u_3}
  {K : Type u_1} {G : Type u_2} {V : Type u_3} [Field K] [CharZero K] [Group G] [Finite G]
  [AddCommGroup V] [_root_.Module K V] [FiniteDimensional K V] (ρ : Representation K G V)
  (hρ : Function.Injective ⇑ρ) :
  ρ.pseudoreflectionSubgroup = ⊤ ↔
    ∃ f,
      (∀ (i : Fin (Module.finrank K V)),
          ∃ d,
            0 < d ∧ ↑(f i) ∈ TauCeti.SymmetricAlgebra.homogeneousSubmodule K (Module.Dual K V) d) ∧
        Function.Bijective ⇑(MvPolynomial.aeval f)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Chevalley–Shephard–Todd theorem (`Representation.exists_bijective_aeval_symmetricAlgebraInvariants_dual_of_pseudoreflectionSubgroup_eq_top`)](the-chevalley-shephard-todd-theorem-representati-2.md)
- [The converse of the Chevalley–Shephard–Todd theorem](the-converse-of-the-chevalley-shephard-todd-theo.md)

## Lean

Formalized in Tau Ceti as [`Representation.pseudoreflectionSubgroup_eq_top_iff_exists_bijective_aeval_symmetricAlgebraInvariants_dual`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SymmetricAlgebra/ShephardTodd.html#Representation.pseudoreflectionSubgroup_eq_top_iff_exists_bijective_aeval_symmetricAlgebraInvariants_dual).

## Sources

- [Tau Ceti documentation: `Representation.pseudoreflectionSubgroup_eq_top_iff_exists_bijective_aeval_symmetricAlgebraInvariants_dual`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SymmetricAlgebra/ShephardTodd.html#Representation.pseudoreflectionSubgroup_eq_top_iff_exists_bijective_aeval_symmetricAlgebraInvariants_dual)
- [Source of `Representation.pseudoreflectionSubgroup_eq_top_iff_exists_bijective_aeval_symmetricAlgebraInvariants_dual` in TauCeti/RepresentationTheory/SymmetricAlgebra/ShephardTodd.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RepresentationTheory/SymmetricAlgebra/ShephardTodd.lean#L293)
- [Tau Ceti roadmap status: Finite reflection invariants, degrees, and Weyl exponents](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ReflectionInvariantTheory/STATUS.md)
