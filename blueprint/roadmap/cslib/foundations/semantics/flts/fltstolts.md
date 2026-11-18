---
catalog: module
lean: Cslib.FLTS.toLTS, Cslib.FLTS.toLTS_tr, Cslib.FLTS.toLTS_deterministic, Cslib.FLTS.toLTS_imageFinite, Cslib.FLTS.toLTS_mtr
statement: formalized
proof: formalized
---

# FLTSToLTS

`Cslib.Foundations.Semantics.FLTS.FLTSToLTS`, in [Cslib/Foundations/Semantics/FLTS/FLTSToLTS.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/FLTS/FLTSToLTS.lean), by Fabrizio Montesi.

> Converting from `FLTS` to `LTS`

`Cslib.FLTS.toLTS` (definition, [line 22](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/FLTS/FLTSToLTS.lean#L22))

> `FLTS` is a special case of `LTS`.

```lean
def toLTS (flts : FLTS State Label) : LTS State Label
```

`Cslib.FLTS.toLTS_tr` (theorem, [line 30](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/FLTS/FLTSToLTS.lean#L30))

> `FLTS.toLTS` correctly characterises transitions.

```lean
theorem toLTS_tr {flts : FLTS State Label} {s1 : State} {μ : Label} {s2 : State} :
  flts.toLTS.Tr s1 μ s2 ↔ flts.tr s1 μ = s2
```

`Cslib.FLTS.toLTS_deterministic` (instance, [line 35](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/FLTS/FLTSToLTS.lean#L35))

> The transition system of a FLTS is deterministic.

```lean
instance toLTS_deterministic (flts : FLTS State Label) : flts.toLTS.Deterministic
```

`Cslib.FLTS.toLTS_imageFinite` (instance, [line 40](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/FLTS/FLTSToLTS.lean#L40))

> The transition system of a FLTS is image-finite.

```lean
instance toLTS_imageFinite (flts : FLTS State Label) : flts.toLTS.ImageFinite
```

`Cslib.FLTS.toLTS_mtr` (theorem, [line 46](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/FLTS/FLTSToLTS.lean#L46))

> Characterisation of multistep transitions.

```lean
theorem toLTS_mtr {flts : FLTS State Label} {s1 : State} {μs : List Label} {s2 : State} :
    flts.toLTS.MTr s1 μs s2 ↔ flts.mtr s1 μs = s2
```

## Depends on

- [Functional Labelled Transition System (FLTS)](basic.md)
- [Labelled Transition System (LTS)](../lts/basic.md)

## Sources

- [Cslib/Foundations/Semantics/FLTS/FLTSToLTS.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/FLTS/FLTSToLTS.lean)
