---
declaration: theorem
origin: cited
lean: TauCeti.exists_mem_span_indVirtualCharacters_isPElementary_not_dvd
statement: formalized
proof: formalized
---

# Brauer's local lemma

For every prime `p` there is a function `ψ : G → ℕ`, none of whose
values is divisible by `p`, whose cast to `k` is an `A`-combination of virtual characters induced
from `p`-elementary subgroups, for every subring `A` of `k` containing the `|G|`-th roots of
unity. It is the sum, over the conjugacy classes of `p`-regular elements `s`, of `orderOf s` times
the induced `p`-section indicator of `s`: at `y` only the class of the `p`-free part of `y`
contributes, and its contribution is prime to `p`.

```lean
TauCeti.exists_mem_span_indVirtualCharacters_isPElementary_not_dvd.{u, v} (k : Type u) {G : Type v}
  [Group G] [Field k] [Finite G] [IsAlgClosed k] [Invertible ↑(Nat.card G)] (p : ℕ)
  [Fact (Nat.Prime p)] :
  ∃ ψ,
    (∀ (y : G), ¬p ∣ ψ y) ∧
      ∀ (A : Subring k),
        (∀ (x : k), x ^ Nat.card G = 1 → x ∈ A) →
          (fun y => ↑(ψ y)) ∈
            Submodule.span ↥A
              ↑(TauCeti.ClassFunction.indVirtualCharacters k G fun S => TauCeti.IsPElementary p ↥S)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_mem_span_indVirtualCharacters_isPElementary_not_dvd`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/Brauer/PSection.html#TauCeti.exists_mem_span_indVirtualCharacters_isPElementary_not_dvd).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_mem_span_indVirtualCharacters_isPElementary_not_dvd`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Induction/Brauer/PSection.html#TauCeti.exists_mem_span_indVirtualCharacters_isPElementary_not_dvd)
- [Source of `TauCeti.exists_mem_span_indVirtualCharacters_isPElementary_not_dvd` in TauCeti/RepresentationTheory/Induction/Brauer/PSection.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Induction/Brauer/PSection.lean#L146)
