---
declaration: theorem
origin: cited
lean: Representation.IsIrreducible.exists_forall_apply_eq_smul
statement: formalized
proof: formalized
---

# Schur's lemma, scalar form

Over an algebraically closed field, a linear endomorphism of a
finite-dimensional irreducible representation commuting with the action is multiplication by a
scalar.  This is `Representation.IsIrreducible.algebraMap_intertwiningMap_bijective_of_isAlgClosed`
read pointwise on an unbundled endomorphism.

```lean
Representation.IsIrreducible.exists_forall_apply_eq_smul.{u_1, u_2, u_3} {k : Type u_1}
  {G : Type u_2} {V : Type u_3} [Field k] [Monoid G] [AddCommGroup V] [_root_.Module k V]
  [IsAlgClosed k] [FiniteDimensional k V] {ρ : Representation k G V} [ρ.IsIrreducible]
  (f : V →ₗ[k] V) (hf : ∀ (g : G) (v : V), f ((ρ g) v) = (ρ g) (f v)) : ∃ c, ∀ (v : V), f v = c • v
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Representation.IsIrreducible.exists_forall_apply_eq_smul`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Irreducible.html#Representation.IsIrreducible.exists_forall_apply_eq_smul).

## Sources

- [Tau Ceti documentation: `Representation.IsIrreducible.exists_forall_apply_eq_smul`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Irreducible.html#Representation.IsIrreducible.exists_forall_apply_eq_smul)
- [Source of `Representation.IsIrreducible.exists_forall_apply_eq_smul` in TauCeti/RepresentationTheory/Irreducible.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Irreducible.lean#L361)
