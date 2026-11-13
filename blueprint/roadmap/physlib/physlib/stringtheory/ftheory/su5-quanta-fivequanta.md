---
declaration: module
origin: cited
lean: FTheory.SU5.FiveQuanta, FTheory.SU5.FiveQuanta.toFluxesFive, FTheory.SU5.FiveQuanta.toCharges, FTheory.SU5.FiveQuanta.toChargeMap, FTheory.SU5.FiveQuanta.toChargeMap_of_not_mem, FTheory.SU5.FiveQuanta.reduce, FTheory.SU5.FiveQuanta.reduce_nodup, FTheory.SU5.FiveQuanta.reduce_dedup
statement: formalized
proof: formalized
---

# Quanta of 5-d representations

The module `Physlib.StringTheory.FTheory.SU5.Quanta.FiveQuanta`, [Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean): 46 declarations, 9 with a docstring.

## i. Overview

> The 5-bar representations of the `SU(5)×U(1)` carry
> the quantum numbers of their `U(1)` charges and their fluxes.
>
> In this module we define the data structure for these quanta and
> properties thereof.

## ii. Key results

> - `FiveQuanta` is the type of quanta of 5-bar representations.
> - `FiveQuanta.toFluxesFive` is the underlying `FluxesFive` of a `FiveQuanta`.
> - `FiveQuanta.toCharges` is the underlying Multiset charges of a `FiveQuanta`.
> - `FiveQuanta.reduce` is the reduction of a `FiveQuanta` which adds together
>   all the fluxes corresponding to the same charge (i.e. representation).
> - `FiveQuanta.liftCharges` given a charge `c` the `FiveQuanta` which have
>   charge `c` and no exotics or zero fluxes.
> - `FiveQuanta.anomalyCoefficient` is the anomaly coefficient associated with a `FiveQuanta`.

## iv. References

> * Rational F-Theory GUTs without exotics (arXiv:1401.5084), Anomaly cancellation
>   conditions. [ref: arxiv\_1401\_5084]

## A. The definition of `FiveQuanta`

**`FTheory.SU5.FiveQuanta`**, an abbrev, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L101).

> The quanta of 5-bar representations corresponding to a multiset of
> `(q, M, N)` for each particle. `(M, N)` are defined in the `FluxesFive` module.

```lean
abbrev FiveQuanta (𝓩 : Type := ℤ) : Type
```

### A.1. The map to underlying fluxes

**`FTheory.SU5.FiveQuanta.toFluxesFive`**, a def, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L114).

> The underlying `FluxesFive` from a `FiveQuanta`.

```lean
def toFluxesFive (x : FiveQuanta 𝓩) : FluxesFive
```

### A.2. The map to underlying charges

**`FTheory.SU5.FiveQuanta.toCharges`**, a def, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L123).

> The underlying Multiset charges from a `FiveQuanta`.

```lean
def toCharges (x : FiveQuanta 𝓩) : Multiset 𝓩
```

### A.3. The map from charges to fluxes

**`FTheory.SU5.FiveQuanta.toChargeMap`**, a def, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L133).

> The map which takes a charge to the overall flux it
> corresponds to in a `FiveQuanta`.

```lean
def toChargeMap [DecidableEq 𝓩] (x : FiveQuanta 𝓩) : 𝓩 → Fluxes
```

**`FTheory.SU5.FiveQuanta.toChargeMap_of_not_mem`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L136).

```lean
lemma toChargeMap_of_not_mem [DecidableEq 𝓩] (x : FiveQuanta 𝓩) {z : 𝓩} (h : z ∉ x.toCharges) :
    x.toChargeMap z = 0
```

## B. The reduction of a `FiveQuanta`

**`FTheory.SU5.FiveQuanta.reduce`**, a def, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L156).

> The `reduce` of `FiveQuanta` is a new `FiveQuanta` with all the fluxes
> corresponding to the same charge (i.e. representation) added together.

```lean
def reduce (x : FiveQuanta 𝓩) : FiveQuanta 𝓩
```

### B.1. The reduced `FiveQuanta` has no duplicate elements

**`FTheory.SU5.FiveQuanta.reduce_nodup`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L165).

```lean
lemma reduce_nodup (x : FiveQuanta 𝓩) : x.reduce.Nodup
```

**`FTheory.SU5.FiveQuanta.reduce_dedup`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L170).

```lean
lemma reduce_dedup (x : FiveQuanta 𝓩) : x.reduce.dedup = x.reduce
```

### B.2. The underlying charges of the reduced `FiveQuanta` are the deduped charges

**`FTheory.SU5.FiveQuanta.reduce_toCharges`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L179).

```lean
lemma reduce_toCharges (x : FiveQuanta 𝓩) : x.reduce.toCharges = x.toCharges.dedup
```

### B.3. Membership condition on the reduced `FiveQuanta`

**`FTheory.SU5.FiveQuanta.mem_reduce_iff`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L188).

```lean
lemma mem_reduce_iff (x : FiveQuanta 𝓩) (p : 𝓩 × Fluxes) :
    p ∈ x.reduce ↔ p.1 ∈ x.toCharges ∧
      p.2 = ((x.filter (fun f => f.1 = p.1)).map (fun y => y.2)).sum
```

### B.4. Filter of the reduced `FiveQuanta` by a charge

**`FTheory.SU5.FiveQuanta.reduce_filter`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L200).

```lean
lemma reduce_filter (x : FiveQuanta 𝓩) (q : 𝓩) (h : q ∈ x.toCharges) :
    x.reduce.filter (fun f => f.1 = q) =
    {(q, ((x.filter (fun f => f.1 = q)).map (fun y => y.2)).sum)}
```

### B.5. The reduction is idempotent

**`FTheory.SU5.FiveQuanta.reduce_reduce`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L212).

```lean
lemma reduce_reduce (x : FiveQuanta 𝓩) :
    x.reduce.reduce = x.reduce
```

### B.6. Preservation of certain sums under reduction

**`FTheory.SU5.FiveQuanta.reduce_sum_eq_sum_toCharges`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L229).

```lean
lemma reduce_sum_eq_sum_toCharges {M} [AddCommMonoid M] (x : FiveQuanta 𝓩) (f : 𝓩 → Fluxes →+ M) :
    (x.reduce.map fun (q5, x) => f q5 x).sum = (x.map fun (q5, x) => f q5 x).sum
```

### B.7. Reduction does nothing if no duplicate charges

**`FTheory.SU5.FiveQuanta.reduce_eq_self_of_ofCharges_nodup`**, a lemma, [line 294](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L294).

```lean
lemma reduce_eq_self_of_ofCharges_nodup (x : FiveQuanta 𝓩) (h : x.toCharges.Nodup) :
    x.reduce = x
```

### B.8. The charge map is preserved by reduction

**`FTheory.SU5.FiveQuanta.reduce_toChargeMap_eq`**, a lemma, [line 325](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L325).

```lean
lemma reduce_toChargeMap_eq (x : FiveQuanta 𝓩) :
    x.reduce.toChargeMap = x.toChargeMap
```

### B.9. A fluxes in the reduced `FiveQuanta` is a sum of fluxes in the original `FiveQuanta`

**`FTheory.SU5.FiveQuanta.mem_powerset_sum_of_mem_reduce_toFluxesFive`**, a lemma, [line 342](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L342).

```lean
lemma mem_powerset_sum_of_mem_reduce_toFluxesFive {F : FiveQuanta 𝓩}
    {f : Fluxes} (hf : f ∈ F.reduce.toFluxesFive) :
    f ∈ (Multiset.powerset F.toFluxesFive).map fun s => s.sum
```

**`FTheory.SU5.FiveQuanta.mem_powerset_sum_of_mem_reduce_toFluxesFive_filter`**, a lemma, [line 354](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L354).

```lean
lemma mem_powerset_sum_of_mem_reduce_toFluxesFive_filter {F : FiveQuanta 𝓩}
    {f : Fluxes} (hf : f ∈ F.reduce.toFluxesFive) :
    f ∈ (F.toFluxesFive.powerset.filter fun s => s ≠ ∅).map fun s => s.sum
```

### B.10. No exotics condition on the reduced `FiveQuanta`

#### B.10.1. Number of chiral `L`

**`FTheory.SU5.FiveQuanta.reduce_numChiralL_of_mem_elemsNoExotics`**, a lemma, [line 386](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L386).

```lean
lemma reduce_numChiralL_of_mem_elemsNoExotics {F : FiveQuanta 𝓩}
    (hx : F.toFluxesFive ∈ FluxesFive.elemsNoExotics) :
    F.reduce.toFluxesFive.numChiralL = 3
```

#### B.10.2. Number of anti-chiral `L`

**`FTheory.SU5.FiveQuanta.reduce_numAntiChiralL_of_mem_elemsNoExotics`**, a lemma, [line 411](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L411).

```lean
lemma reduce_numAntiChiralL_of_mem_elemsNoExotics {F : FiveQuanta 𝓩}
    (hx : F.toFluxesFive ∈ FluxesFive.elemsNoExotics) :
    F.reduce.toFluxesFive.numAntiChiralL = 0
```

#### B.10.3. Number of chiral `D`

**`FTheory.SU5.FiveQuanta.reduce_numChiralD_of_mem_elemsNoExotics`**, a lemma, [line 431](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L431).

```lean
lemma reduce_numChiralD_of_mem_elemsNoExotics {F : FiveQuanta 𝓩}
    (hx : F.toFluxesFive ∈ FluxesFive.elemsNoExotics) :
    F.reduce.toFluxesFive.numChiralD = 3
```

#### B.10.4. Number of anti-chiral `D`

**`FTheory.SU5.FiveQuanta.reduce_numAntiChiralD_of_mem_elemsNoExotics`**, a lemma, [line 455](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L455).

```lean
lemma reduce_numAntiChiralD_of_mem_elemsNoExotics {F : FiveQuanta 𝓩}
    (hx : F.toFluxesFive ∈ FluxesFive.elemsNoExotics) :
    F.reduce.toFluxesFive.numAntiChiralD = 0
```

#### B.10.5. The `NoExotics` condition on the reduced `FiveQuanta`

**`FTheory.SU5.FiveQuanta.reduce_noExotics_of_mem_elemsNoExotics`**, a lemma, [line 474](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L474).

```lean
lemma reduce_noExotics_of_mem_elemsNoExotics {F : FiveQuanta 𝓩}
    (hx : F.toFluxesFive ∈ FluxesFive.elemsNoExotics) :
    F.reduce.toFluxesFive.NoExotics
```

### B.11. Reduce member of `FluxesFive.elemsNoExotics`

**`FTheory.SU5.FiveQuanta.reduce_mem_elemsNoExotics`**, a lemma, [line 487](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L487).

```lean
lemma reduce_mem_elemsNoExotics {F : FiveQuanta 𝓩}
    (hx : F.toFluxesFive ∈ FluxesFive.elemsNoExotics) :
    F.reduce.toFluxesFive ∈ FluxesFive.elemsNoExotics
```

## C. Decomposition of a `FiveQuanta` into basic fluxes

### C.1. Decomposition of fluxes

**`FTheory.SU5.FiveQuanta.decomposeFluxes`**, a def, [line 512](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L512).

> The decomposition of a flux into `⟨1, -1⟩` and `⟨0, 1⟩`.

```lean
def decomposeFluxes (f : Fluxes) : Multiset Fluxes
```

**`FTheory.SU5.FiveQuanta.decomposeFluxes_sum_of_noExotics`**, a lemma, [line 516](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L516).

```lean
lemma decomposeFluxes_sum_of_noExotics (f : Fluxes) (hf : ∃ F ∈ FluxesFive.elemsNoExotics, f ∈ F) :
    (decomposeFluxes f).sum = f
```

### C.2. Decomposition of a `FiveQuanta` (with no exotics)

**`FTheory.SU5.FiveQuanta.decompose`**, a def, [line 531](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L531).

> The decomposition of a `FiveQuanta` into a `FiveQuanta` which has the
> same `reduce` by has fluxes `⟨1, -1⟩` and `⟨0,1⟩` only.

```lean
def decompose (x : FiveQuanta 𝓩) : FiveQuanta 𝓩
```

#### C.2.1. Decomposition distributes over addition

**`FTheory.SU5.FiveQuanta.decompose_add`**, a lemma, [line 540](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L540).

```lean
lemma decompose_add (x y : FiveQuanta 𝓩) :
    (x + y).decompose = x.decompose + y.decompose
```

#### C.2.2. Decomposition commutes with filtering charges

**`FTheory.SU5.FiveQuanta.decompose_filter_charge`**, a lemma, [line 550](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L550).

```lean
lemma decompose_filter_charge [DecidableEq 𝓩] (x : FiveQuanta 𝓩) (q : 𝓩) :
    (x.decompose).filter (fun p => p.1 = q) =
    decompose (x.filter (fun p => p.1 = q))
```

#### C.2.3. Decomposition preserves the charge map

**`FTheory.SU5.FiveQuanta.decompose_toChargeMap`**, a lemma, [line 586](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L586).

```lean
lemma decompose_toChargeMap [DecidableEq 𝓩] (x : FiveQuanta 𝓩)
    (hx : x.toFluxesFive ∈ FluxesFive.elemsNoExotics) :
    x.decompose.toChargeMap = x.toChargeMap
```

#### C.2.4. Decomposition preserves the charges

**`FTheory.SU5.FiveQuanta.decompose_toCharges_dedup`**, a lemma, [line 608](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L608).

```lean
lemma decompose_toCharges_dedup [DecidableEq 𝓩] (x : FiveQuanta 𝓩)
    (hx : x.toFluxesFive ∈ FluxesFive.elemsNoExotics) :
    x.decompose.toCharges.dedup = x.toCharges.dedup
```

#### C.2.5. Decomposition preserves the reduction

**`FTheory.SU5.FiveQuanta.decompose_reduce`**, a lemma, [line 637](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L637).

```lean
lemma decompose_reduce (x : FiveQuanta 𝓩) [DecidableEq 𝓩]
    (hx : x.toFluxesFive ∈ FluxesFive.elemsNoExotics) :
    x.decompose.reduce = x.reduce
```

#### C.2.6. Fluxes of the decomposition of a `FiveQuanta`

**`FTheory.SU5.FiveQuanta.decompose_toFluxesFive`**, a lemma, [line 653](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L653).

```lean
lemma decompose_toFluxesFive (x : FiveQuanta 𝓩)
    (hx : x.toFluxesFive ∈ FluxesFive.elemsNoExotics) :
    x.decompose.toFluxesFive = {⟨1, -1⟩, ⟨1, -1⟩, ⟨1, -1⟩, ⟨0, 1⟩, ⟨0, 1⟩, ⟨0, 1⟩}
```

## D. Lifting charges to `FiveQuanta`

### D.1. `liftCharge c`: multiset of five-quanta for a finite set of charges `c` with no exotics

> This is an efficient definition, we will later show that it gives the correct answer

**`FTheory.SU5.FiveQuanta.liftCharge`**, a def, [line 688](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L688).

> Given a finite set of charges `c` the `FiveQuanta`
> which do not have exotics, duplicate charges or zero fluxes, which map down to `c`.

```lean
def liftCharge (c : Finset 𝓩) : Multiset (FiveQuanta 𝓩)
```

### D.2. FiveQuanta in `liftCharge c` have a finite set of charges `c`

**`FTheory.SU5.FiveQuanta.toCharges_toFinset_of_mem_liftCharge`**, a lemma, [line 705](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L705).

```lean
lemma toCharges_toFinset_of_mem_liftCharge (c : Finset 𝓩) {x : FiveQuanta 𝓩}
    (h : x ∈ liftCharge c) : x.toCharges.toFinset = c
```

### D.3. FiveQuanta in `liftCharge c` have no duplicate charges

**`FTheory.SU5.FiveQuanta.toCharges_nodup_of_mem_liftCharge`**, a lemma, [line 721](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L721).

```lean
lemma toCharges_nodup_of_mem_liftCharge (c : Finset 𝓩) {x : FiveQuanta 𝓩}
    (h : x ∈ liftCharge c) : x.toCharges.Nodup
```

### D.4. Membership in `liftCharge c` iff is reduction of `FiveQuanta` with given fluxes

**`FTheory.SU5.FiveQuanta.exists_toCharges_toFluxesFive_of_mem_liftCharge`**, a lemma, [line 733](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L733).

```lean
lemma exists_toCharges_toFluxesFive_of_mem_liftCharge (c : Finset 𝓩) {x : FiveQuanta 𝓩}
    (h : x ∈ liftCharge c) :
    ∃ a : FiveQuanta 𝓩, a.reduce = x ∧ a.toCharges.toFinset = c ∧ a.toFluxesFive =
      {⟨1, -1⟩, ⟨1, -1⟩, ⟨1, -1⟩, ⟨0, 1⟩, ⟨0, 1⟩, ⟨0, 1⟩}
```

**`FTheory.SU5.FiveQuanta.mem_liftCharge_of_exists_toCharges_toFluxesFive`**, a lemma, [line 749](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L749).

```lean
lemma mem_liftCharge_of_exists_toCharges_toFluxesFive (c : Finset 𝓩) {x : FiveQuanta 𝓩}
    (h : ∃ a : FiveQuanta 𝓩, a.reduce = x ∧ a.toCharges.toFinset = c ∧ a.toFluxesFive =
      {⟨1, -1⟩, ⟨1, -1⟩, ⟨1, -1⟩, ⟨0, 1⟩, ⟨0, 1⟩, ⟨0, 1⟩}) :
    x ∈ liftCharge c
```

**`FTheory.SU5.FiveQuanta.mem_liftCharge_iff_exists`**, a lemma, [line 800](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L800).

```lean
lemma mem_liftCharge_iff_exists (c : Finset 𝓩) {x : FiveQuanta 𝓩} :
    x ∈ liftCharge c ↔ ∃ a : FiveQuanta 𝓩, a.reduce = x ∧
      a.toCharges.toFinset = c ∧ a.toFluxesFive =
      {⟨1, -1⟩, ⟨1, -1⟩, ⟨1, -1⟩, ⟨0, 1⟩, ⟨0, 1⟩, ⟨0, 1⟩}
```

### D.5. FiveQuanta in `liftCharge c` do not have zero fluxes

**`FTheory.SU5.FiveQuanta.hasNoZero_of_mem_liftCharge`**, a lemma, [line 813](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L813).

```lean
lemma hasNoZero_of_mem_liftCharge (c : Finset 𝓩) {x : FiveQuanta 𝓩}
    (h : x ∈ liftCharge c) : x.toFluxesFive.HasNoZero
```

### D.6. FiveQuanta in `liftCharge c` have no exotics

**`FTheory.SU5.FiveQuanta.noExotics_of_mem_liftCharge`**, a lemma, [line 829](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L829).

```lean
lemma noExotics_of_mem_liftCharge (c : Finset 𝓩) (F : FiveQuanta 𝓩)
    (h : F ∈ liftCharge c) :
    F.toFluxesFive.NoExotics
```

### D.7. Membership in `liftCharge c` iff have no exotics, no zero fluxes, and charges `c`

**`FTheory.SU5.FiveQuanta.mem_liftCharge_of_mem_noExotics_hasNoZero`**, a lemma, [line 844](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L844).

```lean
lemma mem_liftCharge_of_mem_noExotics_hasNoZero (c : Finset 𝓩) {x : FiveQuanta 𝓩}
    (h1 : x.toFluxesFive.NoExotics) (h2 : x.toFluxesFive.HasNoZero)
    (h3 : x.toCharges.toFinset = c) (h4 : x.toCharges.Nodup) :
    x ∈ liftCharge c
```

**`FTheory.SU5.FiveQuanta.mem_liftCharge_iff`**, a lemma, [line 862](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L862).

```lean
lemma mem_liftCharge_iff (c : Finset 𝓩) (x : FiveQuanta 𝓩) :
    x ∈ liftCharge c ↔ x.toFluxesFive ∈ FluxesFive.elemsNoExotics
      ∧ x.toCharges.toFinset = c ∧ x.toCharges.Nodup
```

### D.8. `liftCharge c` is preserved under a map if reduced

**`FTheory.SU5.FiveQuanta.map_liftCharge`**, a lemma, [line 882](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L882).

```lean
lemma map_liftCharge {𝓩 𝓩1 : Type}[DecidableEq 𝓩] [DecidableEq 𝓩1] [CommRing 𝓩] [CommRing 𝓩1]
    (f : 𝓩 →+* 𝓩1) (c : Finset 𝓩) (F : FiveQuanta 𝓩) (h : F ∈ liftCharge c) :
    FiveQuanta.reduce (F.map fun y => (f y.1, y.2)) ∈ liftCharge (c.image f)
```

## E. Anomaly cancellation coefficients

### E.1. Anomaly coefficients of a `FiveQuanta`

**`FTheory.SU5.FiveQuanta.anomalyCoefficient`**, a def, [line 919](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L919).

> The anomaly coefficient of a `FiveQuanta` is given by the pair of integers:
> `(∑ᵢ qᵢ Nᵢ, ∑ᵢ qᵢ² Nᵢ)`.
>
> The first components is for the mixed U(1)-MSSM, see equation (22) of arXiv:1401.5084
> [ref: arxiv\_1401\_5084]. The second component is for the mixed U(1)Y-U(1)-U(1) gauge anomaly,
> see equation (23) of arXiv:1401.5084 [ref: arxiv\_1401\_5084].

```lean
def anomalyCoefficient (F : FiveQuanta 𝓩) : 𝓩 × 𝓩
```

### E.2. Anomaly coefficients under a map

**`FTheory.SU5.FiveQuanta.anomalyCoefficient_of_map`**, a lemma, [line 929](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L929).

```lean
lemma anomalyCoefficient_of_map {𝓩 𝓩1 : Type} [CommRing 𝓩] [CommRing 𝓩1]
    (f : 𝓩 →+* 𝓩1) (F : FiveQuanta 𝓩) :
    FiveQuanta.anomalyCoefficient (F.map fun y => (f y.1, y.2) : FiveQuanta 𝓩1) =
    (f.prodMap f) F.anomalyCoefficient
```

### E.3. Anomaly coefficients is preserved under `reduce`

**`FTheory.SU5.FiveQuanta.anomalyCoefficient_of_reduce`**, a lemma, [line 941](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean#L941).

```lean
lemma anomalyCoefficient_of_reduce (F : FiveQuanta 𝓩) [DecidableEq 𝓩] :
    F.reduce.anomalyCoefficient = F.anomalyCoefficient
```

## Depends on

- [The set of charges which minimally allows a potential term](../../particles/supersymmetry/part-02/su5-chargespectrum-minimallyallowsterm-offinset.md)
- [Terms of `FluxesFive` and `FluxesTen` with no chiral exotics](su5-fluxes-noexotics-elems.md)

## Proof depends on

- [Completeness of `Elems` with regard to the `NoExotics` condition](su5-fluxes-noexotics-completeness.md)

## Sources

- [Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/StringTheory/FTheory/SU5/Quanta/FiveQuanta.lean)
