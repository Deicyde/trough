---
declaration: module
origin: cited
lean: FTheory.SU5.TenQuanta, FTheory.SU5.TenQuanta.toFluxesTen, FTheory.SU5.TenQuanta.toCharges, FTheory.SU5.TenQuanta.toChargeMap, FTheory.SU5.TenQuanta.toChargeMap_of_not_mem, FTheory.SU5.TenQuanta.reduce, FTheory.SU5.TenQuanta.reduce_nodup, FTheory.SU5.TenQuanta.reduce_dedup
statement: formalized
proof: formalized
---

# Quanta of 10d representations

The module `Physlib.StringTheory.FTheory.SU5.Quanta.TenQuanta`, [Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean): 48 declarations, 9 with a docstring.

## i. Overview

> The 10d representations of the `SU(5)×U(1)` carry
> the quantum numbers of their `U(1)` charges and their fluxes.
>
> In this module we define the data structure for these quanta and
> properties thereof.

## ii. Key results

> - `TenQuanta` is the type of quanta of 10d representations.
> - `TenQuanta.toFluxesTen` is the underlying `FluxesTen` of a `TenQuanta`.
> - `TenQuanta.toCharges` is the underlying Multiset charges of a `TenQuanta`.
> - `TenQuanta.reduce` is the reduction of a `TenQuanta` which adds together
>   all the fluxes corresponding to the same charge (i.e. representation).
> - `TenQuanta.liftCharges` given a charge `c` the `TenQuanta` which have
>   charge `c` and no exotics or zero fluxes.
> - `TenQuanta.anomalyCoefficient` is the anomaly coefficient associated with a `TenQuanta`.

## iv. References

> * Rational F-Theory GUTs without exotics (arXiv:1401.5084), Anomaly cancellation
>   conditions. [ref: arxiv\_1401\_5084]

## A. The definition of `TenQuanta`

**`FTheory.SU5.TenQuanta`**, an abbrev, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L103).

> The quanta of w0d representations corresponding to a multiset of
> `(q, M, N)` for each particle. `(M, N)` are defined in the `FluxesFive` module.

```lean
abbrev TenQuanta (𝓩 : Type := ℤ) : Type
```

### A.1. The map to underlying fluxes

**`FTheory.SU5.TenQuanta.toFluxesTen`**, a def, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L116).

> The underlying `FluxesTen` from a `TenQuanta`.

```lean
def toFluxesTen (x : TenQuanta 𝓩) : FluxesTen
```

### A.2. The map to underlying charges

**`FTheory.SU5.TenQuanta.toCharges`**, a def, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L125).

> The underlying Multiset charges from a `TenQuanta`.

```lean
def toCharges (x : TenQuanta 𝓩) : Multiset 𝓩
```

### A.3. The map from charges to fluxes

**`FTheory.SU5.TenQuanta.toChargeMap`**, a def, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L135).

> The map which takes a charge to the overall flux it
> corresponds to in a `TenQuanta`.

```lean
def toChargeMap [DecidableEq 𝓩] (x : TenQuanta 𝓩) : 𝓩 → Fluxes
```

**`FTheory.SU5.TenQuanta.toChargeMap_of_not_mem`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L138).

```lean
lemma toChargeMap_of_not_mem [DecidableEq 𝓩] (x : TenQuanta 𝓩) {z : 𝓩} (h : z ∉ x.toCharges) :
    x.toChargeMap z = 0
```

## B. The reduction of a `TenQuanta`

**`FTheory.SU5.TenQuanta.reduce`**, a def, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L156).

> The `reduce` of `TenQuanta` is a new `TenQuanta` with all the fluxes
> corresponding to the same charge (i.e. representation) added together.

```lean
def reduce (x : TenQuanta 𝓩) : TenQuanta 𝓩
```

### B.1. The reduced `TenQuanta` has no duplicate elements

**`FTheory.SU5.TenQuanta.reduce_nodup`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L165).

```lean
lemma reduce_nodup (x : TenQuanta 𝓩) : x.reduce.Nodup
```

**`FTheory.SU5.TenQuanta.reduce_dedup`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L170).

```lean
lemma reduce_dedup (x : TenQuanta 𝓩) : x.reduce.dedup = x.reduce
```

### B.2. The underlying charges of the reduced `TenQuanta` are the deduped charges

**`FTheory.SU5.TenQuanta.reduce_toCharges`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L179).

```lean
lemma reduce_toCharges (x : TenQuanta 𝓩) : x.reduce.toCharges = x.toCharges.dedup
```

### B.3. Membership condition on the reduced `TenQuanta`

**`FTheory.SU5.TenQuanta.mem_reduce_iff`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L188).

```lean
lemma mem_reduce_iff (x : TenQuanta 𝓩) (p : 𝓩 × Fluxes) :
    p ∈ x.reduce ↔ p.1 ∈ x.toCharges ∧
      p.2 = ((x.filter (fun f => f.1 = p.1)).map (fun y => y.2)).sum
```

### B.4. Filter of the reduced `TenQuanta` by a charge

**`FTheory.SU5.TenQuanta.reduce_filter`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L204).

```lean
lemma reduce_filter (x : TenQuanta 𝓩) (q : 𝓩) (h : q ∈ x.toCharges) :
    x.reduce.filter (fun f => f.1 = q) =
    {(q, ((x.filter (fun f => f.1 = q)).map (fun y => y.2)).sum)}
```

### B.5. The reduction is idempotent

**`FTheory.SU5.TenQuanta.reduce_reduce`**, a lemma, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L222).

```lean
lemma reduce_reduce (x : TenQuanta 𝓩) :
    x.reduce.reduce = x.reduce
```

### B.6. Preservation of certain sums under reduction

**`FTheory.SU5.TenQuanta.reduce_sum_eq_sum_toCharges`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L238).

```lean
lemma reduce_sum_eq_sum_toCharges {M} [AddCommMonoid M] (x : TenQuanta 𝓩) (f : 𝓩 → Fluxes →+ M) :
    (x.reduce.map fun (q, x) => f q x).sum = (x.map fun (q, x) => f q x).sum
```

### B.7. Reduction does nothing if no duplicate charges

**`FTheory.SU5.TenQuanta.reduce_eq_self_of_ofCharges_nodup`**, a lemma, [line 303](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L303).

```lean
lemma reduce_eq_self_of_ofCharges_nodup (x : TenQuanta 𝓩) (h : x.toCharges.Nodup) :
    x.reduce = x
```

### B.8. The charge map is preserved by reduction

**`FTheory.SU5.TenQuanta.reduce_toChargeMap_eq`**, a lemma, [line 332](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L332).

```lean
lemma reduce_toChargeMap_eq (x : TenQuanta 𝓩) :
    x.reduce.toChargeMap = x.toChargeMap
```

### B.9. A fluxes in the reduced `TenQuanta` is a sum of fluxes in the original `TenQuanta`

**`FTheory.SU5.TenQuanta.mem_powerset_sum_of_mem_reduce_toFluxesTen`**, a lemma, [line 351](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L351).

```lean
lemma mem_powerset_sum_of_mem_reduce_toFluxesTen {F : TenQuanta 𝓩}
    {f : Fluxes} (hf : f ∈ F.reduce.toFluxesTen) :
    f ∈ (Multiset.powerset F.toFluxesTen).map fun s => s.sum
```

**`FTheory.SU5.TenQuanta.mem_powerset_sum_of_mem_reduce_toFluxesTen_filter`**, a lemma, [line 366](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L366).

```lean
lemma mem_powerset_sum_of_mem_reduce_toFluxesTen_filter {F : TenQuanta 𝓩}
    {f : Fluxes} (hf : f ∈ F.reduce.toFluxesTen) :
    f ∈ (F.toFluxesTen.powerset.filter fun s => s ≠ 0).map fun s => s.sum
```

### B.10. No exotics condition on the reduced `TenQuanta`

#### B.10.1. Number of chiral `U`

**`FTheory.SU5.TenQuanta.reduce_numChiralU_of_mem_elemsNoExotics`**, a lemma, [line 396](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L396).

```lean
lemma reduce_numChiralU_of_mem_elemsNoExotics {F : TenQuanta 𝓩}
    (hx : F.toFluxesTen ∈ FluxesTen.elemsNoExotics) :
    F.reduce.toFluxesTen.numChiralU = 3
```

#### B.10.2. Number of anti-chiral `U`

**`FTheory.SU5.TenQuanta.reduce_numAntiChiralU_of_mem_elemsNoExotics`**, a lemma, [line 424](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L424).

```lean
lemma reduce_numAntiChiralU_of_mem_elemsNoExotics {F : TenQuanta 𝓩}
    (hx : F.toFluxesTen ∈ FluxesTen.elemsNoExotics) :
    F.reduce.toFluxesTen.numAntiChiralU = 0
```

#### B.10.3. Number of chiral `Q`

**`FTheory.SU5.TenQuanta.reduce_numChiralQ_of_mem_elemsNoExotics`**, a lemma, [line 444](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L444).

```lean
lemma reduce_numChiralQ_of_mem_elemsNoExotics {F : TenQuanta 𝓩}
    (hx : F.toFluxesTen ∈ FluxesTen.elemsNoExotics) :
    F.reduce.toFluxesTen.numChiralQ = 3
```

#### B.10.4. Number of anti-chiral `Q`

**`FTheory.SU5.TenQuanta.reduce_numAntiChiralQ_of_mem_elemsNoExotics`**, a lemma, [line 472](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L472).

```lean
lemma reduce_numAntiChiralQ_of_mem_elemsNoExotics {F : TenQuanta 𝓩}
    (hx : F.toFluxesTen ∈ FluxesTen.elemsNoExotics) :
    F.reduce.toFluxesTen.numAntiChiralQ = 0
```

#### B.10.5. Number of chiral `E`

**`FTheory.SU5.TenQuanta.reduce_numChiralE_of_mem_elemsNoExotics`**, a lemma, [line 492](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L492).

```lean
lemma reduce_numChiralE_of_mem_elemsNoExotics {F : TenQuanta 𝓩}
    (hx : F.toFluxesTen ∈ FluxesTen.elemsNoExotics) :
    F.reduce.toFluxesTen.numChiralE = 3
```

#### B.10.6. Number of anti-chiral `E`

**`FTheory.SU5.TenQuanta.reduce_numAntiChiralE_of_mem_elemsNoExotics`**, a lemma, [line 520](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L520).

```lean
lemma reduce_numAntiChiralE_of_mem_elemsNoExotics {F : TenQuanta 𝓩}
    (hx : F.toFluxesTen ∈ FluxesTen.elemsNoExotics) :
    F.reduce.toFluxesTen.numAntiChiralE = 0
```

#### B.10.7. The `NoExotics` condition on the reduced `TenQuanta`

**`FTheory.SU5.TenQuanta.reduce_noExotics_of_mem_elemsNoExotics`**, a lemma, [line 540](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L540).

```lean
lemma reduce_noExotics_of_mem_elemsNoExotics {F : TenQuanta 𝓩}
    (hx : F.toFluxesTen ∈ FluxesTen.elemsNoExotics) :
    F.reduce.toFluxesTen.NoExotics
```

### B.11. Reduce member of `FLuxesTen.elemsNoExotics`

**`FTheory.SU5.TenQuanta.reduce_mem_elemsNoExotics`**, a lemma, [line 555](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L555).

```lean
lemma reduce_mem_elemsNoExotics {F : TenQuanta 𝓩}
    (hx : F.toFluxesTen ∈ FluxesTen.elemsNoExotics) :
    F.reduce.toFluxesTen ∈ FluxesTen.elemsNoExotics
```

## C. Decomposition of a `TenQuanta` into basic fluxes

### C.1. Decomposition of fluxes

**`FTheory.SU5.TenQuanta.decomposeFluxes`**, a def, [line 581](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L581).

> The decomposition of a relevant flux into `⟨1, 0⟩`, `⟨1, 1⟩` and `⟨1, -1⟩` .

```lean
def decomposeFluxes (f : Fluxes) : Multiset Fluxes
```

**`FTheory.SU5.TenQuanta.decomposeFluxes_sum_of_noExotics`**, a lemma, [line 591](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L591).

```lean
lemma decomposeFluxes_sum_of_noExotics (f : Fluxes) (hf : ∃ F ∈ FluxesTen.elemsNoExotics, f ∈ F) :
    (decomposeFluxes f).sum = f
```

### C.2. Decomposition of a `TenQuanta` (with no exotics)

**`FTheory.SU5.TenQuanta.decompose`**, a def, [line 608](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L608).

> The decomposition of a `TenQuanta` into a `TenQuanta` which has the
> same `reduce` by has fluxes `{⟨1, 0⟩, ⟨1, 0⟩, ⟨1, 0⟩}` or `{⟨1, 1⟩, ⟨1, -1⟩, ⟨1, 0⟩}` only.
>
> This only works for fluxes which have no exotics or zeros.

```lean
def decompose (x : TenQuanta 𝓩) : TenQuanta 𝓩
```

#### C.2.1. Decomposition distributes over addition

**`FTheory.SU5.TenQuanta.decompose_add`**, a lemma, [line 617](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L617).

```lean
lemma decompose_add (x y : TenQuanta 𝓩) :
    (x + y).decompose = x.decompose + y.decompose
```

#### C.2.2. Decomposition commutes with filtering charges

**`FTheory.SU5.TenQuanta.decompose_filter_charge`**, a lemma, [line 627](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L627).

```lean
lemma decompose_filter_charge [DecidableEq 𝓩] (x : TenQuanta 𝓩) (q : 𝓩) :
    (x.decompose).filter (fun p => p.1 = q) =
    decompose (x.filter (fun p => p.1 = q))
```

#### C.2.3. Decomposition preserves the charge map

**`FTheory.SU5.TenQuanta.decompose_toChargeMap`**, a lemma, [line 651](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L651).

```lean
lemma decompose_toChargeMap [DecidableEq 𝓩] (x : TenQuanta 𝓩)
    (hx : x.toFluxesTen ∈ FluxesTen.elemsNoExotics) :
    x.decompose.toChargeMap = x.toChargeMap
```

#### C.2.4. Decomposition preserves the charges

**`FTheory.SU5.TenQuanta.decompose_toCharges_dedup`**, a lemma, [line 674](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L674).

```lean
lemma decompose_toCharges_dedup [DecidableEq 𝓩] (x : TenQuanta 𝓩)
    (hx : x.toFluxesTen ∈ FluxesTen.elemsNoExotics) :
    x.decompose.toCharges.dedup = x.toCharges.dedup
```

#### C.2.5. Decomposition preserves the reduction

**`FTheory.SU5.TenQuanta.decompose_reduce`**, a lemma, [line 703](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L703).

```lean
lemma decompose_reduce (x : TenQuanta 𝓩) [DecidableEq 𝓩]
    (hx : x.toFluxesTen ∈ FluxesTen.elemsNoExotics) :
    x.decompose.reduce = x.reduce
```

#### C.2.6. Fluxes of the decomposition of a `TenQuanta`

**`FTheory.SU5.TenQuanta.decompose_toFluxesTen`**, a lemma, [line 718](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L718).

```lean
lemma decompose_toFluxesTen (x : TenQuanta 𝓩)
    (hx : x.toFluxesTen ∈ FluxesTen.elemsNoExotics) :
    x.decompose.toFluxesTen = {⟨1, 0⟩, ⟨1, 0⟩, ⟨1, 0⟩} ∨
    x.decompose.toFluxesTen = {⟨1, 1⟩, ⟨1, -1⟩, ⟨1, 0⟩}
```

## D. Lifting charges to `TenQuanta`

### D.1. `liftCharge c`: multiset of ten-quanta for a finite set of charges `c` with no exotics

> This is an efficient definition, we will later show that it gives the correct answer

**`FTheory.SU5.TenQuanta.liftCharge`**, a def, [line 758](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L758).

> Given a finite set of charges `c` the `TenQuanta`
> which do not have exotics, duplicate charges or zero fluxes, which map down to `c`.
> This is defined to be as efficient as possible.

```lean
def liftCharge (c : Finset 𝓩) : Multiset (TenQuanta 𝓩)
```

### D.2. TenQuanta in `liftCharge c` have a finite set of charges `c`

**`FTheory.SU5.TenQuanta.toCharge_toFinset_of_mem_liftCharge`**, a lemma, [line 776](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L776).

```lean
lemma toCharge_toFinset_of_mem_liftCharge (c : Finset 𝓩)
    {x : TenQuanta 𝓩} (h : x ∈ liftCharge c) :
    x.toCharges.toFinset = c
```

### D.3. TenQuanta in `liftCharge c` have no duplicate charges

**`FTheory.SU5.TenQuanta.toCharges_nodup_of_mem_liftCharge`**, a lemma, [line 814](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L814).

```lean
lemma toCharges_nodup_of_mem_liftCharge (c : Finset 𝓩) {x : TenQuanta 𝓩}
    (h : x ∈ liftCharge c) : x.toCharges.Nodup
```

### D.4. Membership in `liftCharge c` iff is reduction of `TenQuanta` with given fluxes

**`FTheory.SU5.TenQuanta.exists_toCharges_toFluxesTen_of_mem_liftCharge`**, a lemma, [line 827](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L827).

```lean
lemma exists_toCharges_toFluxesTen_of_mem_liftCharge (c : Finset 𝓩)
    {x : TenQuanta 𝓩} (h : x ∈ liftCharge c) :
    ∃ a : TenQuanta 𝓩, a.reduce = x ∧ a.toCharges.toFinset = c ∧
    (a.toFluxesTen = {⟨1, 0⟩, ⟨1, 0⟩, ⟨1, 0⟩}
    ∨ a.toFluxesTen = {⟨1, 1⟩, ⟨1, -1⟩, ⟨1, 0⟩})
```

**`FTheory.SU5.TenQuanta.mem_liftCharge_of_exists_toCharges_toFluxesTen`**, a lemma, [line 850](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L850).

```lean
lemma mem_liftCharge_of_exists_toCharges_toFluxesTen (c : Finset 𝓩) {x : TenQuanta 𝓩}
    (h :∃ a : TenQuanta 𝓩, a.reduce = x ∧ a.toCharges.toFinset = c ∧
    (a.toFluxesTen = {⟨1, 0⟩, ⟨1, 0⟩, ⟨1, 0⟩}
    ∨ a.toFluxesTen = {⟨1, 1⟩, ⟨1, -1⟩, ⟨1, 0⟩})) :
    x ∈ liftCharge c
```

**`FTheory.SU5.TenQuanta.mem_liftCharge_iff_exists`**, a lemma, [line 937](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L937).

```lean
lemma mem_liftCharge_iff_exists (c : Finset 𝓩) {x : TenQuanta 𝓩} :
    x ∈ liftCharge c ↔
    ∃ a : TenQuanta 𝓩, a.reduce = x ∧ a.toCharges.toFinset = c ∧
    (a.toFluxesTen = {⟨1, 0⟩, ⟨1, 0⟩, ⟨1, 0⟩}
    ∨ a.toFluxesTen = {⟨1, 1⟩, ⟨1, -1⟩, ⟨1, 0⟩})
```

### D.5. TenQuanta in `liftCharge c` do not have zero fluxes

**`FTheory.SU5.TenQuanta.hasNoZero_of_mem_liftCharge`**, a lemma, [line 952](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L952).

```lean
lemma hasNoZero_of_mem_liftCharge (c : Finset 𝓩) {x : TenQuanta 𝓩}
    (h : x ∈ liftCharge c) : x.toFluxesTen.HasNoZero
```

### D.6. TenQuanta in `liftCharge c` have no exotics

**`FTheory.SU5.TenQuanta.noExotics_of_mem_liftCharge`**, a lemma, [line 970](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L970).

```lean
lemma noExotics_of_mem_liftCharge (c : Finset 𝓩) (F : TenQuanta 𝓩)
    (h : F ∈ liftCharge c) :
    F.toFluxesTen.NoExotics
```

### D.7. Membership in `liftCharge c` iff have no exotics, no zero fluxes, and charges `c`

**`FTheory.SU5.TenQuanta.mem_liftCharge_of_mem_noExotics_hasNoZero`**, a lemma, [line 987](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L987).

```lean
lemma mem_liftCharge_of_mem_noExotics_hasNoZero (c : Finset 𝓩) {x : TenQuanta 𝓩}
    (h1 : x.toFluxesTen.NoExotics) (h2 : x.toFluxesTen.HasNoZero)
    (h3 : x.toCharges.toFinset = c) (h4 : x.toCharges.Nodup) :
    x ∈ liftCharge c
```

**`FTheory.SU5.TenQuanta.mem_liftCharge_iff`**, a lemma, [line 1004](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L1004).

```lean
lemma mem_liftCharge_iff (c : Finset 𝓩) (x : TenQuanta 𝓩) :
    x ∈ liftCharge c ↔ x.toFluxesTen ∈ FluxesTen.elemsNoExotics
      ∧ x.toCharges.toFinset = c ∧ x.toCharges.Nodup
```

### D.8. `liftCharge c` is preserved under a map if reduced

**`FTheory.SU5.TenQuanta.map_liftCharge`**, a lemma, [line 1024](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L1024).

```lean
lemma map_liftCharge {𝓩 𝓩1 : Type}[DecidableEq 𝓩] [DecidableEq 𝓩1] [CommRing 𝓩] [CommRing 𝓩1]
    (f : 𝓩 →+* 𝓩1) (c : Finset 𝓩) (F : TenQuanta 𝓩) (h : F ∈ liftCharge c) :
    TenQuanta.reduce (F.map fun y => (f y.1, y.2)) ∈ liftCharge (c.image f)
```

## E. Anomaly cancellation coefficients

### E.1. Anomaly coefficients of a `TenQuanta`

**`FTheory.SU5.TenQuanta.anomalyCoefficient`**, a def, [line 1062](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L1062).

> The anomaly coefficient of a `TenQuanta` is given by the pair of integers:
> `(∑ᵢ qᵢ Nᵢ, 3 * ∑ᵢ qᵢ² Nᵢ)`.
>
> The first components is for the mixed U(1)-MSSM, see equation (22) of arXiv:1401.5084
> [ref: arxiv\_1401\_5084]. The second component is for the mixed U(1)Y-U(1)-U(1) gauge anomaly,
> see equation (23) of arXiv:1401.5084 [ref: arxiv\_1401\_5084].

```lean
def anomalyCoefficient (F : TenQuanta 𝓩) : 𝓩 × 𝓩
```

### E.2. Anomaly coefficients under a map

**`FTheory.SU5.TenQuanta.anomalyCoefficient_of_map`**, a lemma, [line 1072](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L1072).

```lean
lemma anomalyCoefficient_of_map {𝓩 𝓩1 : Type} [CommRing 𝓩] [CommRing 𝓩1]
    (f : 𝓩 →+* 𝓩1) (F : TenQuanta 𝓩) :
    TenQuanta.anomalyCoefficient (F.map fun y => (f y.1, y.2) : TenQuanta 𝓩1) =
    (f.prodMap f) F.anomalyCoefficient
```

### E.3. Anomaly coefficients is preserved under `reduce`

**`FTheory.SU5.TenQuanta.anomalyCoefficient_of_reduce`**, a lemma, [line 1084](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean#L1084).

```lean
lemma anomalyCoefficient_of_reduce [DecidableEq 𝓩] (F : TenQuanta 𝓩) :
    F.reduce.anomalyCoefficient = F.anomalyCoefficient
```

## Depends on

- [The set of charges which minimally allows a potential term](../../particles/supersymmetry/part-02/su5-chargespectrum-minimallyallowsterm-offinset.md)
- [Terms of `FluxesFive` and `FluxesTen` with no chiral exotics](su5-fluxes-noexotics-elems.md)

## Proof depends on

- [Completeness of `Elems` with regard to the `NoExotics` condition](su5-fluxes-noexotics-completeness.md)

## Sources

- [Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/TenQuanta.lean)
