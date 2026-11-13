---
declaration: section
origin: cited
lean: MetaMathlibExt.thue_lemma_general, MetaMathlibExt.thue_lemma
statement: formalized
proof: formalized
---

# Thue's lemma

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/thue-s-lemma/index.html).

## Thue's lemma, general form

Let $a$ and $n$ be integers with $n > 1$ and
$\gcd(a, n) = 1$. Then there exist nonzero integers $x$ and $y$ with $|x| < \sqrt{n}$,
$|y| < \sqrt{n}$ and $x \equiv a y \pmod{n}$. Unlike the source form of Thue's lemma, no lower
bound on $a$ is assumed.

Formalized by `MetaMathlibExt.thue_lemma_general`, a theorem declared in [MathlibExt/NumberTheory/ThueLemma.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ThueLemma.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/thue-s-lemma/index.html#thue-lemma-general).

## Thue's lemma

Let $a$ and $n$ be integers with $a > 1$, $n > 1$ and $\gcd(a, n) = 1$. Then
there exist nonzero integers $x$ and $y$ with $|x| < \sqrt{n}$, $|y| < \sqrt{n}$ and
$x \equiv a y \pmod{n}$.

The hypothesis $a > 1$ follows the source and is not needed for the conclusion.

## Sources

- Bencheng Li, Steven J. Miller, Tudor Popescu, Daniel Sarnecki, and Nawapan Wattanawanichkul, "Modeling Random Walks to Infinity on Primes in Z[√2]", Journal of Integer Sequences 25 (2022), Article 22.6.1, Lemma [Thue's lemma], lines 217–218, <https://cs.uwaterloo.ca/journals/JIS/VOL25/Miller/miller11.tex>. Original: V. Shoup, "A Computational Introduction to Number Theory and Algebra", Cambridge University Press, 2005, p. 43.

Formalized by `MetaMathlibExt.thue_lemma`, a theorem declared in [MathlibExt/NumberTheory/ThueLemma.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ThueLemma.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/thue-s-lemma/index.html#thue-lemma).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Thue's lemma](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/thue-s-lemma/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/thue-s-lemma)
