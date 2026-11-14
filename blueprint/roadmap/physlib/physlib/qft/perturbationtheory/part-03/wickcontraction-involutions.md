---
declaration: module
origin: cited
lean: WickContraction.toInvolution, WickContraction.fromInvolution, WickContraction.fromInvolution_getDual?_isSome, WickContraction.fromInvolution_getDual?_eq_some, WickContraction.fromInvolution_getDual?_get, WickContraction.toInvolution_fromInvolution, WickContraction.fromInvolution_toInvolution, WickContraction.equivInvolution
statement: formalized
proof: formalized
---

# Involution associated with a contraction

The module `Physlib.QFT.PerturbationTheory.WickContraction.Involutions`, [Physlib/QFT/PerturbationTheory/WickContraction/Involutions.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Involutions.lean): 8 declarations, 3 with a docstring.

**`WickContraction.toInvolution`**, a def, [line 27](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Involutions.lean#L27).

> The involution of `Fin n` associated with a Wick contraction `c : WickContraction n` as follows.
> If `i : Fin n` is contracted in `c` then it is taken to its dual, otherwise
> it is taken to itself.

```lean
def toInvolution : {f : Fin n → Fin n // Function.Involutive f}
```

**`WickContraction.fromInvolution`**, a def, [line 36](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Involutions.lean#L36).

> The Wick contraction formed by an involution `f` of `Fin n` by taking as the contracted
> sets of the contraction the orbits of `f` of cardinality `2`.

```lean
def fromInvolution (f : {f : Fin n → Fin n // Function.Involutive f}) : WickContraction n
```

**`WickContraction.fromInvolution_getDual?_isSome`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Involutions.lean#L74).

```lean
lemma fromInvolution_getDual?_isSome (f : {f : Fin n → Fin n // Function.Involutive f})
    (i : Fin n) : ((fromInvolution f).getDual? i).isSome ↔ f.1 i ≠ i
```

**`WickContraction.fromInvolution_getDual?_eq_some`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Involutions.lean#L100).

```lean
lemma fromInvolution_getDual?_eq_some (f : {f : Fin n → Fin n // Function.Involutive f}) (i : Fin n)
    (h : ((fromInvolution f).getDual? i).isSome) :
    ((fromInvolution f).getDual? i) = some (f.1 i)
```

**`WickContraction.fromInvolution_getDual?_get`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Involutions.lean#L109).

```lean
lemma fromInvolution_getDual?_get (f : {f : Fin n → Fin n // Function.Involutive f}) (i : Fin n)
    (h : ((fromInvolution f).getDual? i).isSome) :
    ((fromInvolution f).getDual? i).get h = (f.1 i)
```

**`WickContraction.toInvolution_fromInvolution`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Involutions.lean#L115).

```lean
lemma toInvolution_fromInvolution : fromInvolution c.toInvolution = c
```

**`WickContraction.fromInvolution_toInvolution`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Involutions.lean#L133).

```lean
lemma fromInvolution_toInvolution (f : {f : Fin n → Fin n // Function.Involutive f}) :
    (fromInvolution f).toInvolution = f
```

**`WickContraction.equivInvolution`**, a def, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Involutions.lean#L148).

> The equivalence between Wick contractions for `n` and involutions of `Fin n`.
> The involution of `Fin n` associated with a Wick contraction `c : WickContraction n` as follows.
> If `i : Fin n` is contracted in `c` then it is taken to its dual, otherwise
> it is taken to itself.

```lean
def equivInvolution : WickContraction n ≃ {f : Fin n → Fin n // Function.Involutive f}
```

## Depends on

- [Wick contractions](../part-02/wickcontraction-basic.md)

## Sources

- [Physlib/QFT/PerturbationTheory/WickContraction/Involutions.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Involutions.lean)
