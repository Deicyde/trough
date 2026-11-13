---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.GoldwasserSipser.PubIPGame, MetaMathlibExt.Complexity.KeyTheorems.GoldwasserSipser.PubIP, MetaMathlibExt.Complexity.KeyTheorems.GoldwasserSipser.goldwasser_sipser
statement: formalized
---

# Goldwasser–Sipser theorem

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/goldwasser-sipser-theorem/index.html).

## Public-coin interactive-proof game

The game takes a length cap $c$, a number $k$ of
fresh coins per round, a verifier message function $V_{\mathrm{msg}}$, a verifier decision
function $V_{\mathrm{dec}}$, a prover $P$ mapping pairs of a coin prefix and a transcript (a list
of bitstrings) to bitstrings, an input $x$, a coin string $\rho$, a number $j$ of remaining
rounds, a total number $T$ of rounds and a transcript $t$, and returns a Boolean outcome. If
$j = 0$, the outcome is $V_{\mathrm{dec}}(x, \rho, t)$. Otherwise let $\pi$ be the first
$(T - j + 1) k$ coins of $\rho$ (all of $\rho$ if it is shorter), where $T - j$ is truncated
subtraction ($0$ when $j > T$). The verifier sends $m = V_{\mathrm{msg}}(x, \pi, t)$ and the
prover replies $a = P(\pi, t')$, where $t'$ is $t$ extended by $m$. If both $m$ and $a$ have
length at most $c$, the outcome is that of the game with $j - 1$ remaining rounds, the same
$T$, and transcript $t$ extended by $m$ and then $a$; otherwise the outcome is false.

So the verifier's message and the prover's reply in a round see only the coins revealed up to
that round, while the final decision may use the whole coin string.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.GoldwasserSipser.PubIPGame`, a definition declared in [WantedExt/Complexity/KeyTheorems/GoldwasserSipserWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/GoldwasserSipserWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/goldwasser-sipser-theorem/index.html#pub-ipgame).

## Public-coin interactive proofs

A decision problem $L$ is in $\mathsf{PubIP}$ when there
are polynomials $r$, $q$ and $k$ with natural-number coefficients and polynomial-time functions
$V_{\mathrm{msg}}$ (the verifier's message function) and $V_{\mathrm{dec}}$ (its decision
function) with the following property. For a bitstring $x$, a prover $P$ (an arbitrary function
from pairs of a coin prefix and a transcript to bitstrings) and a coin string $c$, let $G(P, c)$
be the outcome of the public-coin interactive-proof game with message length cap $q(|x|)$,
$k(|x|)$ fresh coins per round, verifier $V_{\mathrm{msg}}$ and $V_{\mathrm{dec}}$, prover $P$,
input $x$, coins $c$, $r(|x|)$ remaining rounds out of $r(|x|)$ total rounds and the empty
initial transcript. Then for every bitstring $x$: if $L(x)$ is true, some prover $P$ makes
$G(P, c)$ true for at least $2/3$ of the coin strings $c \in \{0,1\}^{r(|x|) k(|x|)}$; and if
$L(x)$ is false, every prover $P$ makes $G(P, c)$ true for at most $1/3$ of them.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.GoldwasserSipser.PubIP`, a definition declared in [WantedExt/Complexity/KeyTheorems/GoldwasserSipserWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/GoldwasserSipserWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/goldwasser-sipser-theorem/index.html#pub-ip).

## Goldwasser-Sipser: private coins add no power to interactive proofs

The class
$\mathsf{IP}$ of decision problems with (private-coin) interactive proofs equals the class
$\mathsf{PubIP}$ of decision problems with public-coin interactive proofs with polynomially many
rounds.

## Sources

- S. Goldwasser and M. Sipser, "Private coins versus public coins in interactive proof systems", Proceedings of the Eighteenth Annual ACM Symposium on Theory of Computing (STOC 1986), 59-68 (journal version in Advances in Computing Research 5 (1989), 73-90).

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.GoldwasserSipser.goldwasser_sipser` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/GoldwasserSipserWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/GoldwasserSipserWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/goldwasser-sipser-theorem/index.html#goldwasser-sipser).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Goldwasser–Sipser theorem](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/goldwasser-sipser-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/goldwasser-sipser-theorem)
