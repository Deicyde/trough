---
declaration: section
origin: cited
lean: OAI.LeanBlast.CourtadeKumar.courtadeKumarAndAttainment, OAI.SoftChannel204.fullMain
statement: formalized
proof: formalized
---

# 119. The Courtade–Kumar and Hellinger conjectures

2 manuscripts and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves the Courtade–Kumar conjecture: among Boolean functions of independent uniform bits, a single coordinate retains the most mutual information after independent bit-flip noise. A stronger theorem treats randomized binary summaries at fixed initial information. The Hellinger conjecture is also proved for every Boolean output bias and noise correlation.

## Sharp binary-information contraction on the discrete cube

We prove sharp contraction of the information carried by a binary channel under independent symmetric noise on a uniform discrete cube. At fixed initial information, a noisy coordinate retains the most information. The Boolean specialization resolves the Courtade–Kumar conjecture and gives an output-entropy refinement. We also establish a stronger mean-dependent entropy-production bound. The proof combines an explicit three-point optimizer for the local joining problem, two entropy capacities, and a common-output thinning inequality, followed by dimension induction and integration along the noise semigroup.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Sharp-binary-information-contraction-on-the-discrete-cube-September-24-2026/main.pdf); the Lean below formalizes results from it.

## Hellinger contraction with arbitrary Boolean output bias

We prove the Hellinger conjecture for Boolean functions on the uniform discrete cube, with arbitrary output bias. For a Boolean function of mean *m* and every $\rho\in[-1,1]$, the loss $\sqrt{1-m^2}-\mathbb E\sqrt{1-(T_\rho f)^2}$ is at most $1-\sqrt{1-\rho^2}$, with equality for signed coordinates. The proof combines asymmetric dimension induction, a calibrated noise-semigroup energy estimate, and finite exact arithmetic certificates. The Hellinger inequality also yields the Courtade–Kumar information bound.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Hellinger-contraction-with-arbitrary-Boolean-output-bias-September-24-2026/main.pdf).

## The Lean formalization

The formalization proves sharp contraction of the information carried by a binary channel under independent symmetric noise on a uniform discrete cube. At each fixed initial information level, a noisy coordinate channel attains the maximum retained information. It also proves the refined Boolean bound that accounts for output bias, with strict improvement for nonconstant biased outputs at nonzero noise correlation, and the selected mean-dependent entropy-production inequality.

For Boolean functions this includes the Courtade–Kumar inequality $I(f(X);Y)\le1-h_2(\varepsilon)$ in bits at crossover probability $0\le\varepsilon\le1/2$, where $h_2$ is binary entropy. A coordinate and its complement attain equality.

## Lean: Courtade–Kumar inequality and attainment

Stated in [CourtadeKumar.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/CourtadeKumar.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem courtadeKumarAndAttainment : FullStatement
```

Proved in [lean/OAI/InformationTheory/BooleanNoise/Main.lean, line 60](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/InformationTheory/BooleanNoise/Main.lean#L60).

## Lean: Sharp binary-channel contraction and entropy production

Stated in [SoftChannel204.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SoftChannel204.lean).

```lean
theorem fullMain : FullMain
```

Proved in [lean/OAI/InformationTheory/SoftChannel/Main.lean, line 113](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/InformationTheory/SoftChannel/Main.lean#L113).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/119.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/119.md)
