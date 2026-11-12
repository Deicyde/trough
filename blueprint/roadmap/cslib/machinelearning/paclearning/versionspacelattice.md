---
catalog: module
lean: Cslib.MachineLearning.PACLearning.versionSpace_append, Cslib.MachineLearning.PACLearning.VersionSpaces, Cslib.MachineLearning.PACLearning.mem_versionSpaces_iff, Cslib.MachineLearning.PACLearning.self_mem_versionSpaces, Cslib.MachineLearning.PACLearning.inter_mem_versionSpaces, Cslib.MachineLearning.PACLearning.versionSpaces_subset_powerset, Cslib.MachineLearning.PACLearning.versionSpaces_finite, Cslib.MachineLearning.PACLearning.versionSpaces_ncard_le
statement: formalized
proof: formalized
---

# Version Space Lattice

`Cslib.MachineLearning.PACLearning.VersionSpaceLattice`, in [Cslib/MachineLearning/PACLearning/VersionSpaceLattice.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VersionSpaceLattice.lean), by Dhruv Gupta.

> The collection of all version spaces of a concept
> class is a ∩-closed family with top `C`, the *version space lattice* of Mitchell (1982).
>
> ## Main definitions
>
> - `VersionSpaces C`: the family of all version spaces of `C`, over samples of every size.
>
> ## Main results
>
> - `versionSpace_append`: the version space of an appended sample is the intersection of
>   the version spaces.
> - `self_mem_versionSpaces`, `inter_mem_versionSpaces`: the family contains `C` (top) and
>   is closed under intersection.
> - `versionSpaces_subset_powerset`, `versionSpaces_finite`, `versionSpaces_ncard_le`: every
>   member is a subset of `C` and for a finite class the family is finite of size at most
>   `2 ^ C.ncard`.
>
> ## References
>
> * [Mitchell1977]
> * [Mitchell1982]
> * [Mitchell1997]

`Cslib.MachineLearning.PACLearning.versionSpace_append` (theorem, [line 51](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VersionSpaceLattice.lean#L51))

> *The version-space meet law.* The version space of an appended sample is the
> intersection of the version spaces of the two parts: constraints accumulate by
> intersection.

```lean
theorem versionSpace_append {m n : ℕ} (C : ConceptClass α β)
    (S : LabeledSample α β m) (T : LabeledSample α β n) :
    VersionSpace C (Fin.append S T) = VersionSpace C S ∩ VersionSpace C T
```

`Cslib.MachineLearning.PACLearning.VersionSpaces` (definition, [line 72](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VersionSpaceLattice.lean#L72))

> The family of all version spaces of a concept class, over labeled samples of every
> size.

```lean
def VersionSpaces (C : ConceptClass α β) : Set (ConceptClass α β)
```

`Cslib.MachineLearning.PACLearning.mem_versionSpaces_iff` (theorem, [line 76](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VersionSpaceLattice.lean#L76))

> Membership in the version-space family unfolds to a witnessing sample.

```lean
theorem mem_versionSpaces_iff {C V : ConceptClass α β} :
    V ∈ VersionSpaces C ↔ ∃ (m : ℕ) (S : LabeledSample α β m), V = VersionSpace C S
```

`Cslib.MachineLearning.PACLearning.self_mem_versionSpaces` (theorem, [line 81](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VersionSpaceLattice.lean#L81))

> The whole class is a version space (of the empty sample) which means the family has top `C`.

```lean
theorem self_mem_versionSpaces (C : ConceptClass α β) : C ∈ VersionSpaces C
```

`Cslib.MachineLearning.PACLearning.inter_mem_versionSpaces` (theorem, [line 86](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VersionSpaceLattice.lean#L86))

> The version-space family is closed under intersection (append the witnessing
> samples).

```lean
theorem inter_mem_versionSpaces {C U V : ConceptClass α β}
    (hU : U ∈ VersionSpaces C) (hV : V ∈ VersionSpaces C) :
    U ∩ V ∈ VersionSpaces C
```

`Cslib.MachineLearning.PACLearning.versionSpaces_subset_powerset` (theorem, [line 95](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VersionSpaceLattice.lean#L95))

> Every version space is a subset of the class: the family lives in the powerset
> of `C`.

```lean
theorem versionSpaces_subset_powerset (C : ConceptClass α β) :
    VersionSpaces C ⊆ 𝒫 C
```

`Cslib.MachineLearning.PACLearning.versionSpaces_finite` (theorem, [line 101](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VersionSpaceLattice.lean#L101))

> A finite concept class has finitely many version spaces.

```lean
theorem versionSpaces_finite {C : ConceptClass α β} (hC : C.Finite) :
    (VersionSpaces C).Finite
```

`Cslib.MachineLearning.PACLearning.versionSpaces_ncard_le` (theorem, [line 107](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VersionSpaceLattice.lean#L107))

> A finite concept class has at most `2 ^ C.ncard` version spaces: the lattice embeds
> in the powerset.

```lean
theorem versionSpaces_ncard_le {C : ConceptClass α β} (hC : C.Finite) :
    (VersionSpaces C).ncard ≤ 2 ^ C.ncard
```

## Depends on

- [Version Space](versionspace.md)

## Sources

- [Cslib/MachineLearning/PACLearning/VersionSpaceLattice.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VersionSpaceLattice.lean)
