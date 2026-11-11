---
declaration: section
origin: cited
lean: MetaMathlibExt.SpragueGrundy.smithRemoteness, MetaMathlibExt.SpragueGrundy.smithRemoteness_eq, MetaMathlibExt.SpragueGrundy.smithRemoteness_of_moves_eq_empty
statement: formalized
proof: formalized
---

# Smith's remoteness function

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/smith-s-remoteness-function/index.html).

## Smith's remoteness function

For an impartial game $G$, the remoteness $R(p)$ of a
position $p$ of $G$ is defined by well-founded recursion along moves; the options of $p$ are the
positions reachable from $p$ in one move. If $p$ has no options, then $R(p) = 0$. Otherwise, if
some option $q$ of $p$ has $R(q)$ even, then $R(p)$ is $1$ plus the least even value of $R(q)$
over the options $q$ of $p$; if every option $q$ of $p$ has $R(q)$ odd, then $R(p)$ is $1$ plus
the largest value of $R(q)$ over the options $q$ of $p$.

## Sources

- C. A. B. Smith, *Graphs and composite games*, J. Combin. Theory 1 (1966), 51–81; as recalled in Vladimir Gurvich, Denis Martynov, Vladislav Maximchuk, and Michael Vyalyi, *On Remoteness Functions of Exact Slow k-NIM with k+1 Piles*, INTEGERS 24 (2024), Article G1, Section 1.3.

Formalized by `MetaMathlibExt.SpragueGrundy.smithRemoteness`, a definition declared in [MathlibExt/GameTheory/SmithRemoteness.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GameTheory/SmithRemoteness.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/smith-s-remoteness-function/index.html#smith-remoteness).

## Recursion for Smith's remoteness

Let $G$ be an impartial game, $p$ a position of $G$, and
$R$ the set of remotenesses of the options of $p$ (the positions reachable from $p$ in one move).
If $R$ contains an even number, the remoteness of $p$ is $1$ plus the least even element of $R$;
otherwise, if $R$ is nonempty, it is $1$ plus the largest element of $R$; and if $R$ is empty,
it is $0$.

## Sources

- C. A. B. Smith, *Graphs and composite games*, J. Combin. Theory 1 (1966), 51–81.

Formalized by `MetaMathlibExt.SpragueGrundy.smithRemoteness_eq`, a theorem declared in [MathlibExt/GameTheory/SmithRemoteness.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GameTheory/SmithRemoteness.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/smith-s-remoteness-function/index.html#smith-remoteness-eq).

## Smith's remoteness vanishes at terminal positions

In an impartial game, the remoteness
of a terminal position (a position with no moves) is $0$.

## Sources

- C. A. B. Smith, *Graphs and composite games*, J. Combin. Theory 1 (1966), 51–81.

Formalized by `MetaMathlibExt.SpragueGrundy.smithRemoteness_of_moves_eq_empty`, a theorem declared in [MathlibExt/GameTheory/SmithRemoteness.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GameTheory/SmithRemoteness.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/smith-s-remoteness-function/index.html#smith-remoteness-of-moves-eq-empty).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Smith's remoteness function](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/smith-s-remoteness-function/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GameTheory/combinatorial-games/smith-s-remoteness-function)
