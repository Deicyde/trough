---
catalog: module
lean: Cslib.LTS.toFLTS, Cslib.LTS.toFLTS_mem_tr, Cslib.LTS.toFLTS_mem_mtr, Cslib.LTS.toFLTS_mtr_setImageMultistep
statement: formalized
proof: formalized
---

# LTSToFLTS

`Cslib.Foundations.Semantics.FLTS.LTSToFLTS`, in [Cslib/Foundations/Semantics/FLTS/LTSToFLTS.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/FLTS/LTSToFLTS.lean), by Fabrizio Montesi.

> Converting from `LTS` to `FLTS`

`Cslib.LTS.toFLTS` (definition, [line 22](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/FLTS/LTSToFLTS.lean#L22))

> Converts an `LTS` into an `FLTS` using the subset construction.

```lean
def toFLTS (lts : LTS State Label) : FLTS (Set State) Label
```

`Cslib.LTS.toFLTS_mem_tr` (theorem, [line 27](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/FLTS/LTSToFLTS.lean#L27))

> Characterisation of transitions in `LTS.toFLTS` wrt transitions in the original `LTS`.

```lean
theorem toFLTS_mem_tr {lts : LTS State Label} {S : Set State} {s' : State} {μ : Label} :
  s' ∈ lts.toFLTS.tr S μ ↔ ∃ s ∈ S, lts.Tr s μ s'
```

`Cslib.LTS.toFLTS_mem_mtr` (theorem, [line 35](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/FLTS/LTSToFLTS.lean#L35))

> Characterisation of multistep transitions in `LTS.toFLTS` wrt multistep transitions in the
> original `LTS`.

```lean
theorem toFLTS_mem_mtr {lts : LTS State Label} {S : Set State} {s' : State} {μs : List Label} :
    s' ∈ lts.toFLTS.mtr S μs ↔ ∃ s ∈ S, lts.MTr s μs s'
```

`Cslib.LTS.toFLTS_mtr_setImageMultistep` (theorem, [line 41](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/FLTS/LTSToFLTS.lean#L41))

> Characterisation of multistep transitions in `LTS.toFLTS` as image transitions in `LTS`.

```lean
theorem toFLTS_mtr_setImageMultistep {lts : LTS State Label} :
  lts.toFLTS.mtr = lts.setImageMultistep
```

## Depends on

- [Functional Labelled Transition System (FLTS)](basic.md)
- [Images of sets of states](../lts/setimage.md)

## Sources

- [Cslib/Foundations/Semantics/FLTS/LTSToFLTS.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/FLTS/LTSToFLTS.lean)
