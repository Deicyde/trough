---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.KatzSmallDoublingProgressionsWanted.katzSumset, MathlibExt.Combinatorics.KatzSmallDoublingProgressionsWanted.katzAPSet, MathlibExt.Combinatorics.KatzSmallDoublingProgressionsWanted.conjecture, MathlibExt.Combinatorics.KatzSmallDoublingProgressionsWanted.conjecture_holds
statement: formalized
---

# Progressions in sets of small doubling

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/progressions-in-sets-of-small-doubling/index.html).

## Sumset of a finite set of integers

For a finite set $A \subseteq \mathbb{Z}$, the sumset
$A + A = \{a + b : a, b \in A\}$, a finite set of integers.

## Sources

- [AIM-COMBINATORICS-0211], AIM Problem Lists, Recent trends in additive combinatorics, item 1.5, `aim-combinatorics-notes.json notes[210]`.

Formalized by `MathlibExt.Combinatorics.KatzSmallDoublingProgressionsWanted.katzSumset`, a definition declared in [WantedExt/Combinatorics/KatzSmallDoublingProgressionsWanted.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/KatzSmallDoublingProgressionsWanted.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/progressions-in-sets-of-small-doubling/index.html#katz-sumset).

## Arithmetic progressions in a finite set of integers, as pairs

For a natural number $k$
and a finite set $A \subseteq \mathbb{Z}$, the set of pairs $(a, d)$ of integers such that
$a + i d \in A$ for every natural number $i < k$. The pair $(a, d)$ stands for the $k$-term
arithmetic progression $a, a + d, \dots, a + (k - 1)d$; the difference $d$ may be zero or
negative.

## Sources

- [AIM-COMBINATORICS-0211], AIM Problem Lists, Recent trends in additive combinatorics, item 1.5, `aim-combinatorics-notes.json notes[210]`.

Formalized by `MathlibExt.Combinatorics.KatzSmallDoublingProgressionsWanted.katzAPSet`, a definition declared in [WantedExt/Combinatorics/KatzSmallDoublingProgressionsWanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/KatzSmallDoublingProgressionsWanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/progressions-in-sets-of-small-doubling/index.html#katz-apset).

## Katz's question on progressions in sets of small doubling

For a finite set
$A \subseteq \mathbb{Z}$ write $A + A = \{a + b : a, b \in A\}$. This is the statement that for
every natural number $k \ge 3$ and every real number $C \ge 2$ there is a real number $c > 0$ such
that every finite set $A \subseteq \mathbb{Z}$ with $|A + A| < C|A|$ has at least $c|A|^2$ pairs
$(a, d)$ of integers with $a + i d \in A$ for all natural numbers $i < k$.

Each pair $(a, d)$ is a $k$-term arithmetic progression $a, a + d, \dots, a + (k - 1)d$ in $A$;
pairs with $d = 0$ or $d < 0$ are counted too. The question is Problem 1.5 of the AIM problem
list on additive combinatorics, posed by N. Katz.

## Sources

- [AIM-COMBINATORICS-0211], AIM Problem Lists, Recent trends in additive combinatorics, item 1.5, `aim-combinatorics-notes.json notes[210]`, https://aimath.org/WWN/additivecomb/additivecomb.pdf.

Formalized by `MathlibExt.Combinatorics.KatzSmallDoublingProgressionsWanted.conjecture`, a definition declared in [WantedExt/Combinatorics/KatzSmallDoublingProgressionsWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/KatzSmallDoublingProgressionsWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/progressions-in-sets-of-small-doubling/index.html#conjecture).

## Sets of small doubling contain many arithmetic progressions

For a finite set
$A \subseteq \mathbb{Z}$ write $A + A = \{a + b : a, b \in A\}$. For every natural number $k \ge 3$
and every real number $C \ge 2$ there is a real number $c > 0$ such that every finite set
$A \subseteq \mathbb{Z}$ with $|A + A| < C|A|$ has at least $c|A|^2$ pairs $(a, d)$ of integers
with $a + i d \in A$ for all natural numbers $i < k$.

This answers Katz's Problem 1.5 affirmatively. On the AIM additive-combinatorics list B. Green
observes that a large subset of $A$ is Freiman-isomorphic to a dense subset of
$\mathbb{Z}/p\mathbb{Z}$ (Ruzsa's lemma), and Szemerédi's theorem with Varnavides averaging gives
$\gg_{k,C} |A|^2$ $k$-term progressions. The pairs with $d = 0$ counted here cover small sets.

## Sources

- AIM workshop problem list, Additive combinatorics (additivecomb.pdf), Problem 1.5 (N. Katz) and remark by B. Green, https://aimath.org/WWN/additivecomb/additivecomb.pdf.

Stated but not proved: `MathlibExt.Combinatorics.KatzSmallDoublingProgressionsWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/KatzSmallDoublingProgressionsWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/KatzSmallDoublingProgressionsWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/progressions-in-sets-of-small-doubling/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Progressions in sets of small doubling](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/progressions-in-sets-of-small-doubling/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/progressions-in-sets-of-small-doubling)
