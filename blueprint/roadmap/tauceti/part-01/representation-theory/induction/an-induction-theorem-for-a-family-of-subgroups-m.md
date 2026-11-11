---
declaration: theorem
origin: cited
lean: TauCeti.mem_virtualCharacters_iff_forall_comp_subtype
statement: formalized
proof: formalized
---

# An induction theorem for a family of subgroups makes restriction to that family detect the virtual characters

For a class function on `G`, membership in the virtual-character lattice is
equivalent to membership of all its restrictions to the family.

The forward direction `TauCeti.comp_subtype_mem_virtualCharacters` needs no hypothesis on the
family; the hypothesis is used only for the converse.

```lean
TauCeti.mem_virtualCharacters_iff_forall_comp_subtype.{u, v} {k : Type u} {G : Type v} [Field k]
  [Group G] [Finite G] {P : Subgroup G → Prop}
  (hP : TauCeti.ClassFunction.indVirtualCharacters k G P = TauCeti.virtualCharacters k G)
  {f : G → k} (hf : f ∈ TauCeti.ClassFunction k G) :
  f ∈ TauCeti.virtualCharacters k G ↔
    ∀ (S : Subgroup G), P S → (fun s => f ↑s) ∈ TauCeti.virtualCharacters k ↥S
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [An induction theorem is a single membership](an-induction-theorem-is-a-single-membership.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.mem_virtualCharacters_iff_forall_comp_subtype`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/Ideal.html#TauCeti.mem_virtualCharacters_iff_forall_comp_subtype).

## Sources

- [Tau Ceti documentation: `TauCeti.mem_virtualCharacters_iff_forall_comp_subtype`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/Ideal.html#TauCeti.mem_virtualCharacters_iff_forall_comp_subtype)
- [Source of `TauCeti.mem_virtualCharacters_iff_forall_comp_subtype` in TauCeti/RepresentationTheory/Induction/Ideal.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Induction/Ideal.lean#L413)
