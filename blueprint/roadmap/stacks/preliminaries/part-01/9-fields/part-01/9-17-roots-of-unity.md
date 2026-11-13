---
declaration: section
origin: cited
lean: isCyclic_and_card_dvd_of_encard_pow_eq_one_le_of_dvd
statement: formalized
proof: formalized
---

# 9.17 Roots of unity

Section 9.17 of the Stacks Project, [Tag 09HW](https://stacks.math.columbia.edu/tag/09HW). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09HX, a lemma

[Tag 09HX](https://stacks.math.columbia.edu/tag/09HX) in the Stacks Project.

**`isCyclic_and_card_dvd_of_encard_pow_eq_one_le_of_dvd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/GroupTheory/SpecificGroups/CyclicOrderDividing.lean, line 27](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/GroupTheory/SpecificGroups/CyclicOrderDividing.lean#L27). The attribute's comment: “cyclic of order dividing n; finiteness deduced”.

> A group of exponent dividing `n` in which, for every `d ∣ n`, at most `d` elements satisfy
> `x ^ d = 1` is cyclic of order dividing `n`. The cardinality bound is stated with `Set.encard`,
> so finiteness of `G` is deduced rather than assumed.

```lean
theorem isCyclic_and_card_dvd_of_encard_pow_eq_one_le_of_dvd
    {G : Type*} [Group G] {n : ℕ} (hpow : ∀ x : G, x ^ n = 1)
    (hcard : ∀ d, d ∣ n → {x : G | x ^ d = 1}.encard ≤ d) :
    IsCyclic G ∧ Nat.card G ∣ n
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 9.17, Tag 09HW](https://stacks.math.columbia.edu/tag/09HW)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
