---
declaration: section
origin: cited
lean: OAI.DimensionTen.exists_channel_fin21, OAI.DimensionTen.main_pair
statement: formalized
proof: formalized
---

# 272. Entanglement without distillable secret key

1 manuscript and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Constructs an entangled state on $\mathbb C^{10}\otimes\mathbb C^{10}$ with zero distillable secret key for the specified local-instrument protocols that complete almost surely. These allow joint local processing and authenticated two-way public communication, with no other shared private resource and an eavesdropper holding the input purification and public record. A trace-preserving PPT channel on $M_{21}(\mathbb C)$ whose square is not entanglement breaking disproves Christandl's PPT-square conjecture.

## Entanglement with zero distillable secret key in local dimension ten

We construct an entangled state on $\mathbb C^{10}\otimes\mathbb C^{10}$ with zero distillable secret key for the local-instrument protocols specified here. They allow joint processing of all copies and unlimited two-way public communication, with the input as the only shared private resource and an eavesdropper holding a purification and the complete public record. The construction also disproves the unrestricted two-map PPT-composition conjecture. A separate trace-preserving PPT channel on $M_{21}(\mathbb C)$ has a square that is not entanglement breaking.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Entanglement-with-zero-distillable-secret-key-in-local-dimension-ten-September-27-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The paper's entanglement construction yields counterexamples to PPT-composition claims. The linked formalization covers these consequences: two explicitly specified PPT maps on $10\times10$ complex matrices have a composition that is not entanglement breaking, and the nonzero Choi matrix of that composition has no nonzero product vector in its range. A separate trace-preserving PPT channel on $21\times21$ matrices has a square that is not entanglement breaking.

The paper's zero-distillable-secret-key statement is outside these two selected Comparator statements.

## Lean: PPT channel on dimension 21 whose square is not entanglement breaking

Stated in [DimensionTenChannel.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/DimensionTenChannel.lean).

```lean
theorem exists_channel_fin21 :
    ∃ Θ : ChannelCompletion.Map (Fin 21) (Fin 21),
      ChannelCompletion.PPT Θ ∧ ChannelCompletion.TracePreserving Θ ∧
        ¬ ChannelCompletion.EntanglementBreaking (Θ.comp Θ)
```

Proved in [lean/OAI/Analysis/Quantum/DimensionTen/Channel.lean, line 140](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/Quantum/DimensionTen/Channel.lean#L140).

## Lean: Dimension-ten PPT pair with non-entanglement-breaking composition

Stated in [DimensionTenPair.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/DimensionTenPair.lean).

```lean
theorem main_pair :
    ∃ Φ₁ Φ₂ : Mat 10 → Mat 10,
      Φ₁ = phiOne ∧ Φ₂ = phiTwo ∧ PPT Φ₁ ∧ PPT Φ₂ ∧
      (let Z := choi (Φ₂ ∘ Φ₁)
       Z ≠ 0 ∧
       (∀ u v : Fin 10 → ℂ, ∀ w : Fin 10 × Fin 10 → ℂ,
         Z *ᵥ w = productVector u v → u = 0 ∨ v = 0) ∧
       ¬ EntanglementBreaking (Φ₂ ∘ Φ₁))
```

Proved in [lean/OAI/Analysis/Quantum/DimensionTen/Main.lean, line 90](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/Quantum/DimensionTen/Main.lean#L90).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/272.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/272.md)
