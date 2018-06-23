(ns prob-46)

;; It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

;; 9 = 7 + 2×1^2
;; 15 = 7 + 2×2^2
;; 21 = 3 + 2×3^2
;; 25 = 7 + 2×3^2
;; 27 = 19 + 2×2^2
;; 33 = 31 + 2×1^2

;; It turns out that the conjecture was false.

;; What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

(defn divides?
  [a b]
  (zero? (mod b a)))

(defn prime*?
  [n]
  (let [possible-divisors (range 2 (inc (Math/round (Math/sqrt n))))
        divs (map #(divides? % n) possible-divisors)]

    (or (= n 2)
        (= (set divs) #{false}))))

(def prime? (memoize prime*?))

(def primes
  (filter prime? (drop 2 (range))))

(def double-squares
  (map #(Math/round (* 2 (Math/pow % 2))) (range)))

(contains? #{1 2} 3)

(defn goldbach-gen
  [n]
  (remove nil?
          (for [np (take-while #(< % n) primes)]
            (if (contains? (set (take-while #(< % n) double-squares)) (- n np))
              np))))

#_(defn goldbach?
  [n]
  (or (prime? n)
      (pos? (count (goldbach-gen n)))))

(doseq [n (range 3 10000 2)]
  (if (and (not (prime? n))
           (empty? (goldbach-gen n)))

    (println n " is a counter example")))

;; Local Variables:
;; compile-command: "lumo -d prob_46.clj"
;; End:
