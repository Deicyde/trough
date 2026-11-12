---
declaration: section
origin: cited
lean: OAI.DilutedSpinGlass.mezard_parisi
statement: formalized
proof: formalized
---

# 221. The Mézard–Parisi formula for diluted spin glasses

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves the Mézard–Parisi hierarchical cavity formula for Poisson-diluted even-arity Ising models satisfying the Panchenko–Talagrand factorization and positivity assumptions, with only first-moment integrability. The limiting free energy equals the infimum over finite-depth hierarchical trial laws. This includes the Viana–Bray model, symmetric diluted even-spin models, and weighted soft even-*K* satisfiability.

## The Mézard–Parisi formula for diluted spin glasses

We prove the Mézard–Parisi hierarchical cavity formula for diluted even-arity Ising models in the Panchenko–Talagrand class. This resolves the variational equality conjecture for that class: the limiting pressure equals the infimum of the trial functional over all finite hierarchy depths and trial laws. Only first moments of the interaction and external field are required.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-Mezard-Parisi-formula-for-diluted-spin-glasses-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization proves the Mézard–Parisi hierarchical cavity formula for diluted even-arity Ising models in the Panchenko–Talagrand class. Under the class's factorization, independence, integrability, and positivity assumptions, the finite-system pressure converges to the infimum of the trial functional over all finite hierarchy depths and trial laws. The arity is any even integer at least two and the interaction density is positive.

## Lean: Mézard–Parisi variational equality for diluted even-arity spin glasses

Stated in [DilutedSpin.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/DilutedSpin.lean).

```lean
theorem mezard_parisi {p : ℕ} (M : Model p) (hM : Admissible M) :
    Tendsto (pressure M) atTop (𝓝 (variationalValue M))
```

Proved in [lean/OAI/Probability/DilutedSpin/Main.lean, line 12](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/DilutedSpin/Main.lean#L12).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/221.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/221.md)
