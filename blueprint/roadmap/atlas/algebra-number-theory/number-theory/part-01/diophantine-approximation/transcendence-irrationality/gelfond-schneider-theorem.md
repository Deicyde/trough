---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.TranscendenceWanted.gelfondSchneider_complex_exp, MathlibExt.NumberTheory.TranscendenceWanted.gelfondSchneider_real_rpow
statement: formalized
proof: formalized
---

# Gelfond–Schneider theorem

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/transcendence-irrationality/gelfond-schneider-theorem/index.html).

## Gelfond–Schneider theorem for every value of a complex power

Let $a, b \in \mathbb{C}$
be algebraic over $\mathbb{Q}$ with $a \neq 1$ and $b \notin \mathbb{Q}$, and let $z \in \mathbb{C}$
satisfy $e^z = a$. Then $e^{bz}$ is transcendental over $\mathbb{Q}$.

The hypothesis $e^z = a$ already implies $a \neq 0$. Taking $z = \log a + 2 \pi i n$, where
$\log a$ is the principal logarithm and $n$ is an integer, recovers every branch of $a^b$.

## Sources

- A. O. Gelfond, *Sur le septième problème de Hilbert* (1934), and T. Schneider, *Transzendenzuntersuchungen periodischer Funktionen I. Transzendenz von Potenzen*, J. Reine Angew. Math. 172 (1935), 65–69, DOI 10.1515/crll.1935.172.65. Explicit arbitrary- and principal-branch applications occur in arXiv:2311.11127v1, arXiv:2607.23662v1, and arXiv:2608.17545v1. The Lean formalization in arXiv:2603.24823v1 states only the principal `Complex.cpow` value; this declaration records the arbitrary-logarithm form.

Formalized by `MathlibExt.NumberTheory.TranscendenceWanted.gelfondSchneider_complex_exp`, a theorem declared in [MathlibExt/NumberTheory/GelfondSchneider.lean, line 2184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/GelfondSchneider.lean#L2184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/transcendence-irrationality/gelfond-schneider-theorem/index.html#gelfond-schneider-complex-exp).

## Gelfond–Schneider theorem for real powers

Let $\alpha$ and $\beta$ be real numbers that
are algebraic over $\mathbb{Q}$, with $\alpha > 0$, $\alpha \neq 1$ and $\beta$ irrational. Then
the real power $\alpha^\beta$ is transcendental over $\mathbb{Q}$.

## Sources

- A. O. Gelfond, Sur le septième problème de Hilbert, Dokl. Akad. Nauk SSSR 2 (1934) 1–6 and T. Schneider 1935 independent; textbook in Baker, Transcendental Number Theory

Formalized by `MathlibExt.NumberTheory.TranscendenceWanted.gelfondSchneider_real_rpow`, a theorem declared in [MathlibExt/NumberTheory/GelfondSchneider.lean, line 2454](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/GelfondSchneider.lean#L2454). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/transcendence-irrationality/gelfond-schneider-theorem/index.html#gelfond-schneider-real-rpow).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Gelfond–Schneider theorem](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/transcendence-irrationality/gelfond-schneider-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/diophantine-approximation/transcendence-irrationality/gelfond-schneider-theorem)
