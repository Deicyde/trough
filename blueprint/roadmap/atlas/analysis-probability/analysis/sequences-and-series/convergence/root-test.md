---
declaration: section
origin: cited
lean: summable_norm_of_root_test_tendsto_lt_one, summable_of_root_test_tendsto_lt_one, not_summable_of_root_test_tendsto_gt_one
statement: formalized
proof: formalized
---

# Root test

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/root-test/index.html).

## Cauchy's root test, absolute convergence case

Let $f : \mathbb{N} \to \alpha$ be a
sequence in a normed additive commutative group $\alpha$. If $\|f(n)\|^{1/n}$ tends to a real
limit $l$ with $l < 1$ as $n \to \infty$, then the series $\sum_n \|f(n)\|$ converges.

Formalized by `summable_norm_of_root_test_tendsto_lt_one`, a theorem declared in [MathlibExt/Analysis/SpecificLimits/RootTest.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecificLimits/RootTest.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/root-test/index.html#summable-norm-of-root-test-tendsto-lt-on).

## Cauchy's root test, convergence case

Let $f : \mathbb{N} \to \alpha$ be a sequence in a
complete normed additive commutative group $\alpha$. If $\|f(n)\|^{1/n}$ tends to a real limit
$l$ with $l < 1$ as $n \to \infty$, then $f$ is summable, that is, the series $\sum_n f(n)$
converges unconditionally.

Formalized by `summable_of_root_test_tendsto_lt_one`, a theorem declared in [MathlibExt/Analysis/SpecificLimits/RootTest.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecificLimits/RootTest.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/root-test/index.html#summable-of-root-test-tendsto-lt-one).

## Cauchy's root test, divergence case

Let $f : \mathbb{N} \to \alpha$ be a sequence in a
seminormed additive commutative group $\alpha$. If $\|f(n)\|^{1/n}$ tends to a real limit $l$ with
$l > 1$ as $n \to \infty$, then $f$ is not summable, that is, the series $\sum_n f(n)$ does not
converge unconditionally.

Formalized by `not_summable_of_root_test_tendsto_gt_one`, a theorem declared in [MathlibExt/Analysis/SpecificLimits/RootTest.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecificLimits/RootTest.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/root-test/index.html#not-summable-of-root-test-tendsto-gt-one).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Root test](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/convergence/root-test/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/sequences-and-series/convergence/root-test)
