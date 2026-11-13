---
declaration: section
origin: cited
lean: MetaMathlibExt.infinitely_many_primes_fibonacci_pseudoprime, MetaMathlibExt.pocklington_prime_power_criterion, MetaMathlibExt.proth_theorem
statement: formalized
proof: formalized
---

# Primality tests and pseudoprimes: its own results

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/index.html).

Primality criteria (Proth, Pocklington, Lucas–Lehmer), Fermat, Lucas, Frobenius and strong pseudoprimes, Carmichael and Korselt numbers.

## Infinitely many Fibonacci pseudoprimes at twice-prime indices

Let $F_m$ denote the
$m$-th Fibonacci number. There are infinitely many primes $p$ such that $n = F_{2p}$ satisfies
$n > 1$, $n$ is not prime, and $n$ divides $F_{n - \left(\frac{5}{n}\right)}$, where
$\left(\frac{5}{n}\right)$ is the Jacobi symbol. In other words, $F_{2p}$ is a Fibonacci
pseudoprime: a composite number $n$ that divides $F_{n - \left(\frac{5}{n}\right)}$.

## Sources

- Y. Hamahata and Y. Kokubun, "Cipolla Pseudoprimes," Journal of Integer Sequences 10 (2007), Article 07.8.6, Corollary 4 [Lehmer], lines 321–324 (Fibonacci-pseudoprime definition at lines 313–318), https://cs.uwaterloo.ca/journals/JIS/VOL10/Hamahata2/hamahata44.tex

Formalized by `MetaMathlibExt.infinitely_many_primes_fibonacci_pseudoprime`, a theorem declared in [MathlibExt/NumberTheory/FibonacciPseudoprimeInfinitude.lean, line 597](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/FibonacciPseudoprimeInfinitude.lean#L597). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/index.html#infinitely-many-primes-fibonacci-pseudop).

## Pocklington's criterion for $N = Kp^e + 1$

Let $N$, $K$ and $e$ be natural numbers and
let $p$ be a prime, with $0 < K < p^e$ and $N = Kp^e + 1$. If some natural number $a$ satisfies
$a^{N-1} \equiv 1 \pmod{N}$ and $\gcd\big(a^{(N-1)/p} - 1, N\big) = 1$, where $(N-1)/p$ is the
quotient of $N - 1$ by $p$ rounded down and $a^{(N-1)/p} - 1$ is truncated at $0$, then $N$ is
prime.

Proof: The proof follows Pocklington's standard least-prime-factor order argument, from
Pocklington (1914) as stated by Grau and Oller-Marcen, arXiv:1011.4836v3, lines 60-69.

## Sources

- Pocklington (1914), as stated in Grau and Oller-Marcen, "A primality test for Kp^n+1 numbers", arXiv:1011.4836v3, lines 60-69, which give the complete condition, including gcd(a^((N-1)/p)-1,N)=1. The source's integer witness a ∈ ℤ is represented here by a natural residue representative a : ℕ, using Nat.ModEq and Nat.gcd with natural subtraction in the exponents.

Formalized by `MetaMathlibExt.pocklington_prime_power_criterion`, a theorem declared in [MathlibExt/NumberTheory/PocklingtonPrimePowerCriterion.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PocklingtonPrimePowerCriterion.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/index.html#pocklington-prime-power-criterion).

## Proth's theorem

Let $h$ and $k$ be natural numbers with $h$ odd and $h < 2^k$, and let
$N = h \cdot 2^k + 1$. Then $N$ is prime if and only if there is a residue class $a$ modulo $N$
with $a^{(N-1)/2} = -1$ in $\mathbb{Z}/N\mathbb{Z}$.

Proof: The forward implication uses a nonsquare and Euler's criterion; the reverse uses Proth's
least-prime-factor order argument. Sources: Proth (1878), p. 926, and the Wikipedia exposition.

## Sources

- https://en.wikipedia.org/wiki/Proth%27s_theorem

Formalized by `MetaMathlibExt.proth_theorem`, a theorem declared in [MathlibExt/NumberTheory/ProthTheorem.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ProthTheorem.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/index.html#proth-theorem).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Primality tests and pseudoprimes](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/primes-primality/primality-tests-pseudoprimes)
