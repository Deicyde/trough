---
declaration: theorem
origin: cited
lean: Representation.inertia_quotient_pseudoreflectionSubgroup_eq_bot
statement: formalized
proof: formalized
---

# The residual quotient has trivial inertia in codimension one

Let `ρ` be a faithful
representation of a finite group `G` on a space `V`, and let `H` be its
pseudoreflection subgroup. Then `G ⧸ H` acts on the polynomial invariants `Sym(V*)^H`, and the
inertia group of every height-one prime of `Sym(V*)^H` for this action is trivial. Geometrically,
the residual quotient `V/H → V/G` by `G ⧸ H` has trivial inertia at every codimension-one point.

```lean
Representation.inertia_quotient_pseudoreflectionSubgroup_eq_bot.{u_1, u_2, u_3} {K : Type u_1}
  {G : Type u_2} {V : Type u_3} [Field K] [Group G] [AddCommGroup V] [_root_.Module K V]
  (ρ : Representation K G V) [Finite G] (hρ : Function.Injective ⇑ρ)
  (P :
    Ideal
      ↥(FixedPoints.subalgebra K (SymmetricAlgebra K (Module.Dual K V))
          ↥ρ.pseudoreflectionSubgroup))
  [P.IsPrime] (hP : P.height = 1) : Ideal.inertia (G ⧸ ρ.pseudoreflectionSubgroup) P = ⊥
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Serre's criterion](../../ring-theory/part-01/ideal/serres-criterion.md)

## Lean

Formalized in Tau Ceti as [`Representation.inertia_quotient_pseudoreflectionSubgroup_eq_bot`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SymmetricAlgebra/Inertia.html#Representation.inertia_quotient_pseudoreflectionSubgroup_eq_bot).

## Sources

- [Tau Ceti documentation: `Representation.inertia_quotient_pseudoreflectionSubgroup_eq_bot`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SymmetricAlgebra/Inertia.html#Representation.inertia_quotient_pseudoreflectionSubgroup_eq_bot)
- [Source of `Representation.inertia_quotient_pseudoreflectionSubgroup_eq_bot` in TauCeti/RepresentationTheory/SymmetricAlgebra/Inertia.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RepresentationTheory/SymmetricAlgebra/Inertia.lean#L270)
- [Tau Ceti roadmap status: Finite reflection invariants, degrees, and Weyl exponents](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ReflectionInvariantTheory/STATUS.md)
